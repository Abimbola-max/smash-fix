from rest_framework import permissions, generics, serializers, status
from rest_framework.response import Response

from bids.models import Bid
from bids.serializers import BidSerializer
from job.models import RepairJob
from user.permissions import IsRepairer, IsCustomer


class BidListView(generics.ListAPIView):
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'customer':
            return Bid.objects.filter(job__customer=user)
        elif user.user_type == 'repairer':
            return Bid.objects.filter(repairer=user)
        return Bid.objects.none()

class BidCreateView(generics.CreateAPIView):
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        job_id = self.request.data.get('job')
        job = RepairJob.objects.get(id=job_id)

        if job.status not in ['open', 'bidding']:
            raise serializers.ValidationError("Bidding is closed for this job.")

        if job.status == 'open':
            job.status = 'bidding'
            job.save()

        serializer.save(repairer=self.request.user, job=job, status='pending')

class MyBidsListView(generics.ListAPIView):
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated, IsRepairer]

    def get_queryset(self):
        return Bid.objects.filter(repairer=self.request.user)

class BidUpdateView(generics.UpdateAPIView):
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bid.objects.all()

    def patch(self, request, *args, **kwargs):
        bid = self.get_object()
        if bid.status != 'pending':
            return Response({'error': 'Cannot update bid unless it is pending'}, status=400)
        return super().patch(request, *args, **kwargs)

class BidAcceptRejectView(generics.UpdateAPIView):
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    queryset = Bid.objects.all()

    def update(self, request, *args, **kwargs):
        bid = self.get_object()
        if bid.job.customer != request.user:
            return Response({'error': 'Not your job.'}, status=status.HTTP_403_FORBIDDEN)
        action = request.data.get('action')
        if action == 'accept':
            bid.status = 'accepted'
        elif action == 'reject':
            bid.status = 'rejected'
        else:
            return Response({'error': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)
        bid.save()
        return Response(BidSerializer(bid).data)