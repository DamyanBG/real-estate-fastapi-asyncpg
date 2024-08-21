from enum import Enum


class UserRole(Enum):
    user = "user"
    admin = "admin"
    guest = "guest"


class AuthProvider(Enum):
    internal = "internal"
    google = "google"
