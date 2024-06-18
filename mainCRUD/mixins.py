from rest_framework import permissions

from .permissions import isStaffPermissionEditor

class isStaffPermissionEditor():
    permissions_classes = [permissions.IsAdminUser, isStaffPermissionEditor]