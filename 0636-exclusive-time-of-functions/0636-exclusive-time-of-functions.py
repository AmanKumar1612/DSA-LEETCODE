class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, event_type, time_str = log.split(":")
            fn_id = int(fn_id_str)
            curr_time = int(time_str)

            if event_type == "start":
                if stack:
                    # Credit elapsed time to the currently running function
                    ans[stack[-1]] += curr_time - prev_time
                stack.append(fn_id)
                prev_time = curr_time
            else:
                # End of current function (inclusive of curr_time)
                ans[stack.pop()] += curr_time - prev_time + 1
                prev_time = curr_time + 1

        return ans