def insert_at_any_pos(head, pos, x):
    new_node = Node(x)

    if pos == 0:
        new_node.next = head
        return new_node

    current = head
    current_pos = 0

    while current is not None and current_pos < pos - 1:
        current = current.next
        current_pos += 1

    if current is None:
        return head

    new_node.next = current.next
    current.next = new_node

    return head
