from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a client
        return request.user.is_authenticated and request.user.is_client


class IsFreelancer(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a freelancer
        return request.user.is_authenticated and request.user.is_freelancer
