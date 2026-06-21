"""
╔══════════════════════════════════════════════════════════════════════╗
║           Learning Minimax & Alpha-Beta Pruning                    ║
║                                                                    ║
║  Two algorithms that let AI play perfect games by "thinking ahead" ║
╚══════════════════════════════════════════════════════════════════════╝

We'll explore using a small game tree as our "game."

RULES:
  • MAX (▲) wants the HIGHEST final number  — "the maximizer"
  • MIN (▼) wants the LOWEST  final number  — "the minimizer"
  • Leaf nodes are terminal — they have a fixed score.

Our tree (leaf values are the scores):

               ▲  MAX  <── root
             ┌──┴──┐
            ▼     ▼
           MIN   MIN
          ╱  ╲  ╱  ╲
         3    5 2    7
"""

import sys

# ═════════════════════════════════════════════════════════════════════
#  PART 1 — Represent the game tree
# ═════════════════════════════════════════════════════════════════════


class Node:
    """A node in the game tree."""

    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children or []  # child nodes
        self.value = value  # only leaf nodes have a value

    def is_leaf(self):
        return self.value is not None

    def label(self):
        """Show type + value for leaf, or just type for internal node."""
        if self.is_leaf():
            return f"LEAF({self.name}={self.value})"
        return f"{self.name}"


# Build the example tree
#                  ▲ root
#                ┌─┴─┐
#               A    B
#              ╱ ╲  ╱ ╲
#             3   5 2   7
root = Node(
    "root",
    [
        Node(
            "A",
            [
                Node("A1", value=3),
                Node("A2", value=5),
            ],
        ),
        Node(
            "B",
            [
                Node("B1", value=2),
                Node("B2", value=7),
            ],
        ),
    ],
)


# ═════════════════════════════════════════════════════════════════════
#  PART 2 — Minimax (vanilla)
# ═════════════════════════════════════════════════════════════════════


def minimax(node, depth, is_max, indent=""):
    """
    Classic minimax.
    Returns the value the current player can guarantee from this position.
    """
    if node.is_leaf() or depth == 0:
        val = node.value if node.is_leaf() else 0
        print(f"{indent}  ──→ {node.label()} = {val}")
        return val

    player = "▲ MAX" if is_max else "▼ MIN"
    print(f"{indent}  {player} at {node.name}:")

    best = -float("inf") if is_max else float("inf")
    for child in node.children:
        print(f"{indent}    trying {child.name}...")
        val = minimax(child, depth - 1, not is_max, indent + "      ")
        if is_max:
            best = max(best, val)
        else:
            best = min(best, val)
        print(f"{indent}    → {child.name} = {val}, best so far = {best}")

    print(f"{indent}  → {player} at {node.name} picks best = {best}")
    return best


# ═════════════════════════════════════════════════════════════════════
#  PART 3 — Alpha-Beta Pruning
# ═════════════════════════════════════════════════════════════════════


def alphabeta(node, depth, alpha, beta, is_max, indent=""):
    """
    Minimax + pruning.
    α = best MAX can guarantee (starts at -∞)
    β = best MIN can guarantee (starts at +∞)
    When α ≥ β, further search is pointless — prune it!
    """
    if node.is_leaf() or depth == 0:
        val = node.value if node.is_leaf() else 0
        print(f"{indent}  ──→ {node.label()} = {val}")
        return val

    player = "▲ MAX" if is_max else "▼ MIN"
    ab = f"α={alpha}" if is_max else f"β={beta}"
    print(f"{indent}  {player} at {node.name}  [{ab}]")

    best = -float("inf") if is_max else float("inf")

    for child in node.children:
        print(f"{indent}    trying {child.name}...")
        val = alphabeta(child, depth - 1, alpha, beta, not is_max, indent + "      ")

        if is_max:
            best = max(best, val)
            alpha = max(alpha, best)
        else:
            best = min(best, val)
            beta = min(beta, best)

        print(f"{indent}    → {child.name} = {val}, best = {best}", end="")
        if is_max:
            print(f", α={alpha}")
        else:
            print(f", β={beta}")

        print("Alpha & Beta:", alpha, beta)
        # Pruning check
        if alpha >= beta:
            print(
                f"{indent}    ⚡ α ≥ β ({alpha} ≥ {beta}) → PRUNE rest of {node.name}!"
            )
            break

    print(f"{indent}  → {player} at {node.name} returns best = {best}")
    return best


# ═════════════════════════════════════════════════════════════════════
#  PART 4 — Run the tutorial
# ═════════════════════════════════════════════════════════════════════


def print_tree(node, indent=""):
    """Print the tree structure with ASCII art."""
    if node.is_leaf():
        print(f"{indent}📄 {node.name} = {node.value}")
    else:
        print(f"{indent}🔷 {node.name}")
        for i, child in enumerate(node.children):
            is_last = i == len(node.children) - 1
            connector = "└── " if is_last else "├── "
            print_tree(child, indent + connector)


# ---- INTRO ----
print()
print_tree(root)
print()
print("  ▲ MAX wants HIGH numbers → chooses the max child")
print("  ▼ MIN wants LOW  numbers → chooses the min child")
print("  📄 Leaf = final score from that position")
print()
print("  ▶ Auto-running in 3 seconds...\n")

# ---- MINIMAX DEMO ----
print("\n" + "=" * 60)
print('  1️⃣  MINIMAX  —  "what if both play perfectly?"')
print("=" * 60)
print("""
  Minimax simulates every possible move.
  At MAX nodes, pick the child with the HIGHEST value.
  At MIN nodes, pick the child with the LOWEST  value.
  Values propagate up from the leaves.\n""")
print()

mm_result = minimax(root, depth=10, is_max=True, indent="")

print(f"\n  ✅ FINAL: Root value = {mm_result}")
print(f"     → MAX can guarantee a score of {mm_result}")
print(f"     → MAX should choose the child that leads to this value.\n")

print()

# ---- ALPHA-BETA DEMO ----
print("\n" + "=" * 60)
print('  2️⃣  ALPHA-BETA PRUNING  —  "cut irrelevant branches"')
print("=" * 60)
print("""
  Same as minimax, but smarter.
  Keep track of:
    α (alpha) = the best MAX can already guarantee
    β (beta)  = the best MIN can already guarantee

  If α ≥ β at a MIN node, the MIN player
  would never let the game go there — so skip it!

  This gives the EXACT SAME result, but faster.\n""")


ab_result = alphabeta(
    root, depth=10, alpha=-float("inf"), beta=float("inf"), is_max=True, indent=""
)

print(f"\n  ✅ FINAL: Root value = {ab_result} (same as minimax!)")
print()
print("  💡 Takeaway: Alpha-Beta prunes branches that")
print("     can't possibly affect the final decision,")
print("     giving the same answer with less work.")


# ═════════════════════════════════════════════════════════════════════
#  PART 5 — Bonus: Apply it to Nim
# ═════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  3️⃣  REAL-WORLD EXAMPLE:  Nim (the take-away game)")
print("=" * 60)
print("""
  Rules: There's a heap of N tokens.
         Each turn, take 1 or 2 tokens.
         Whoever takes the LAST token wins.

  Let's see what minimax says for different starting sizes.\n""")


class NimState:
    def __init__(self, count, is_max_turn):
        self.count = count
        self.is_max_turn = is_max_turn

    def is_terminal(self):
        return self.count == 0

    def evaluate(self):
        # Terminal: the player whose turn it is has NO moves → they lose
        if self.count == 0:
            return -1 if self.is_max_turn else 1  # MAX's perspective
        return 0

    def legal_moves(self):
        return [t for t in (1, 2) if t <= self.count]

    def make_move(self, move):
        return NimState(self.count - move, not self.is_max_turn)


def minimax_nim(state, depth):
    """Minimax for Nim (no trace — just the numbers)."""
    if depth == 0 or state.is_terminal():
        return state.evaluate()

    if state.is_max_turn:
        best = -float("inf")
        for m in state.legal_moves():
            best = max(best, minimax_nim(state.make_move(m), depth - 1))
        return best
    else:
        best = float("inf")
        for m in state.legal_moves():
            best = min(best, minimax_nim(state.make_move(m), depth - 1))
        return best


for tokens in range(1, 13):
    s = NimState(tokens, is_max_turn=True)  # MAX to move
    val = minimax_nim(s, depth=20)
    verdict = "WIN  🏆" if val == 1 else "LOSE 💀"
    print(f"  {tokens:2d} tokens → {verdict}  (value = {val:2d})")

print()
print("  Pattern: multiples of 3 are losing for the player to move.")
print("  If it's your turn with N % 3 == 0 → you lose (with perfect play).")
print("  Otherwise → you can force a win by taking N % 3 tokens.")
print()
print("━" * 60)
print("  That's minimax & alpha-beta in a nutshell! 🎯")
print("━" * 60)
