class ToolInputError(Exception):
    """Raised when the user provides invalid input to a tool."""
    pass


class ToolExecutionError(Exception):
    """Raised when a tool fails to execute properly."""
    pass
