class Solution:
  def checkIfPangram(self, sentence: str) -> bool:
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    for c in sentence:
        alphabet.discard(c)

    return len(alphabet) == 0