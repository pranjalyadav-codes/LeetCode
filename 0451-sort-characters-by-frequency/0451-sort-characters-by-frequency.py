class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        # Step 1: Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(s) + 1)]

        # Step 3: Group characters by frequency
        for ch, count in freq.items():
            buckets[count].append(ch)

        # Step 4: Build result from highest frequency
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for ch in buckets[i]:
                result.append(ch * i)

        return ''.join(result)
