class Solution:
    def minWindow(self, s: str, t: str) -> str:
        occur_order = deque()
        word_freq = {}

        for c in t:
            word_freq[c] = word_freq.get(c, 0) + 1

        completed = len(word_freq)
        left = 0
        right = 0

        min_window = float('inf')
        for i, c in enumerate(s):
            if c in word_freq:
                word_freq[c] -= 1
                occur_order.append((c, i))
                if word_freq[c] < 0:
                    while word_freq[occur_order[0][0]] < 0:
                        word_freq[occur_order[0][0]] += 1
                        occur_order.popleft()
                        win_len = occur_order[-1][1] - occur_order[0][1] + 1
                        if win_len < min_window:
                            left = occur_order[0][1]
                            right = occur_order[-1][1]
                            min_window = win_len

                elif word_freq[c] == 0:
                    completed -= 1

                if completed == 0:
                    left = occur_order[0][1]
                    right = occur_order[-1][1]
                    min_window = occur_order[-1][1] - occur_order[0][1] + 1
                    completed -= 1

        if completed > 0:
            return ""

        return s[left:right+1]


