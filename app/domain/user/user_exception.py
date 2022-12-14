class UserNotFoundError(Exception):
    message = "The user you spcecified does not exist."

    def __str__(self):
        return UserNotFoundError.message


class UsersNotFoundError(Exception):
    message = "No Users were found."

    def __str__(self):
        return UsersNotFoundError.message
