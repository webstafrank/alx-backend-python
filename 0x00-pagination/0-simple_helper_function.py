def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for a page of data.

    Parameters:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start and end index for the range.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

