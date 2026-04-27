from __future__ import annotations
from typing import Optional
from node import Node

def list_reverse(first: Optional[Node]) -> Optional[Node]:
    """Reverses a singly-linked list in place with explicit type hints."""
    prev = None
    curr = first
    while curr is not None:
        nxt = curr.next    
        curr.next = prev   
        prev = curr        
        curr = nxt         
    return prev            
