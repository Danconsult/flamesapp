from collections import Counter
class FlamesApp:
    def __init__(self,girl_name,boy_name) -> None:
        self.girl_name = girl_name
        self.boy_name = boy_name

    def app_logic(self):
        count_str1 = Counter(self.girl_name)
        count_str2 = Counter(self.boy_name)

        # Find common letters and sum their occurrences in both strings
        common_chars = set(count_str1.keys()) & set(count_str2.keys())
        total_occurrences = sum(min(count_str1[char], count_str2[char]) for char in common_chars)
        len_girlname = len(self.girl_name) - total_occurrences
        len_boyname = len(self.boy_name) - total_occurrences
        sum_names = len_girlname + len_boyname
        num_flames = 6
        if sum_names > 6:
            sum_names = sum_names % num_flames
            # Flames app rules
        self.girl_name = self.girl_name.capitalize()
        self.boy_name = self.boy_name.capitalize()
        if sum_names == 0:
            return f"{self.girl_name} and {self.boy_name} may be gay"
        elif sum_names == 1:
            return f"{self.girl_name} and {self.boy_name} are friends"
        elif sum_names == 2:
            return f"{self.girl_name} and {self.boy_name} are lovers"
        elif sum_names == 3:
            return f"{self.girl_name} and {self.boy_name} admire each others"
        elif sum_names == 4:
            return f"{self.girl_name} and {self.boy_name} are married"
        elif sum_names == 5:
            return f"{self.girl_name} and {self.boy_name} are enemies"
        elif sum_names == 6:
            return f"{self.girl_name} and {self.boy_name} are singles"
        else:
            return "An error occurs"