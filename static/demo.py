import xml.etree.ElementTree as ET
from collections import Counter
from sklearn.neighbors import NearestNeighbors

class Case:
    def __init__(self, case_id, problem, solution):
        self.case_id = case_id
        self.problem = problem
        self.solution = solution

class CBRSystem:
    def __init__(self):
        self.case_base = []
        self.main_index = {}
        self.secondary_index = {}

    def add_case(self, case):
        self.case_base.append(case)
        self.update_indexes(case)

    def update_indexes(self, case):
        # 更新主索引和副索引
        for keyword in case.problem:
            if keyword not in self.main_index:
                self.main_index[keyword] = []
            self.main_index[keyword].append(case)

        for keyword in set(case.problem):  # 使用set去重，减小副索引的规模
            if keyword not in self.secondary_index:
                self.secondary_index[keyword] = []
            self.secondary_index[keyword].append(case)

    def retrieve_case(self, new_problem, k=3):
        # 使用主索引、副索引和关键字法结合的检索策略

        # 步骤1：主索引检索
        main_index_matches = self.main_index_search(new_problem)

        # 步骤2：副索引检索
        secondary_index_matches = self.secondary_index_search(new_problem)

        # 步骤3：关键字法检索
        keyword_matches = self.keyword_search(new_problem)

        # 合并检索结果
        all_matches = main_index_matches + secondary_index_matches + keyword_matches

        # 步骤4：K最近邻法检索
        if all_matches:
            return self.knn_search(new_problem, all_matches, k)
        else:
            return None

    def main_index_search(self, new_problem):
        # 主索引检索
        main_index_matches = [case for keyword in new_problem if keyword in self.main_index
                              for case in self.main_index[keyword]]
        return main_index_matches

    def secondary_index_search(self, new_problem):
        # 副索引检索
        secondary_index_matches = [case for keyword in set(new_problem) if keyword in self.secondary_index
                                   for case in self.secondary_index[keyword]]
        return secondary_index_matches

    def keyword_search(self, new_problem):
        # 关键字法检索
        keyword_matches = [case for case in self.case_base if all(keyword in case.problem for keyword in new_problem)]
        return keyword_matches

    def knn_search(self, new_problem, candidates, k):
        # K最近邻法检索
        knn_data = [case.problem for case in candidates]
        knn_model = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(knn_data)
        distances, indices = knn_model.kneighbors([new_problem])
        return [candidates[i] for i in indices[0]]

# 从XML文件中加载案例数据
def load_cases_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    cases = []
    for case_elem in root.findall('case'):
        case_id = int(case_elem.find('case_id').text)
        problem = [elem.tag for elem in case_elem.find('problem')]
        solution = case_elem.find('solution').text
        cases.append(Case(case_id, problem, solution))

    return cases
# 示例用法
xml_file = 'cases.xml'  # 替换为你的XML文件路径
cases = load_cases_from_xml(xml_file)
cbr_system = CBRSystem()
# 添加案例到系统
for case in cases:
    cbr_system.add_case(case)
# 模拟从XML文件中解析新问题
new_problem_xml = "<root><tag1/><tag2/><tag3/></root>"
new_problem = [elem.tag for elem in ET.fromstring(new_problem_xml)]
# 解决新问题
solution = cbr_system.retrieve_case(new_problem, k=2)
if solution:
    print(f"新问题的解决方案是：{solution[0].solution}，案例ID：{solution[0].case_id}")
else:
    print("未找到匹配的案例。")
