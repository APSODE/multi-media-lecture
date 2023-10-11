class FileCreator:
    @staticmethod
    def create_txt(your_name: str):
        ascii_str_list = ["ABC", "abc"]
        ksx1001_str_list = ["가나다", "각난닫", f"\"{your_name}\""]
        utf16be_str_list = ["ABC", "abc", "가나다", "각난닫", f"\"{your_name}\""]
        utf8_str_list = ["ABC", "abc", "가나다", "각난닫", f"\"{your_name}\""]

        result_dir = "result\\"

        for target_str in ascii_str_list:
            with open(result_dir + target_str + "_ascii.txt", "w", encoding = "ascii") as f:
                f.write(target_str)

        for target_str in ksx1001_str_list:
            with open(result_dir + target_str.replace("\"", "") + "_ksx1001.txt", "w", encoding = "ksx1001") as f:
                f.write(target_str)

        for target_str in utf16be_str_list:
            with open(result_dir + target_str.replace("\"", "") + "_utf16be.txt", "w", encoding = "utf-16be") as f:
                f.write(target_str)

        for target_str in utf8_str_list:
            with open(result_dir + target_str.replace("\"", "") + "_utf8.txt", "w", encoding = "utf8") as f:
                f.write(target_str)


class Convertor:
    @staticmethod
    def convert_to_ascii_hex(target_string: str) -> str:
        return "".join([hex(ord(c)).upper() + " " for c in target_string])

    @staticmethod
    def convert_to_utf16_be_hex(target_string: str) -> str:
        return "".join([e.hex().upper() + " " for e in [c.encode(encoding = "utf-16be") for c in [s for s in target_string]]])

    @staticmethod
    def convert_to_utf8_hex(target_string: str) -> str:
        return "".join([e.hex().upper() + " " for e in [c.encode(encoding = "utf-8") for c in [s for s in target_string]]])

    @staticmethod
    def convert_to_ksx1001_hex(target_string: str) -> str:
        return "".join([e.hex().upper() + " " for e in [c.encode(encoding = "ksx1001") for c in [s for s in target_string]]])


if __name__ == '__main__':
    # 사용법
    # 1. name 변수에 자기 이름을 지정한다.
    # 2. 인코딩된 txt파일이 필요할 경우 I_NEED_ENCODE_FILE의 값을 True으로 변경한다.
    # 3. Convertor.py 파일을 실행한다.
    # 3-1. Pycharm인 경우 shift + f10 단축키를 사용하거나 실행버튼 클릭
    # 3-2. cmd를 이용하는 경우 해당 소스파일이 있는 디렉토리에서 py Convetor.py 입력후 엔터

    name = "이건보"  # 이름 입력
    name_quotation = "\"" + name + "\""  # 이름에 쌍따옴표를 추가함
    # 이 쌍따옴표는 각각 UTF-16BE : 0022, UTF-8 : 22, KS X 1001 : 22 의 값을 가지므로 과제 파일에 알아서 적절히 기록하기 바람

    I_NEED_ENCODE_FILE = False
    if I_NEED_ENCODE_FILE:
        # 파이썬 open()함수에서 encoding을 거칠 경우 대문자 소문자가 자동으로 소문자로 바뀌므로 데이터가 다를수 있음
        FileCreator.create_txt(name)

    print(f"ABC - ASCII : {Convertor.convert_to_ascii_hex('ABC')}")
    print(f"abc - ASCII : {Convertor.convert_to_ascii_hex('abc')}")
    print(f"가나다 - KS X 1001 : {Convertor.convert_to_ksx1001_hex('가나다')}")
    print(f"각난닫 - KS X 1001 : {Convertor.convert_to_ksx1001_hex('각난닫')}")
    print(f"{name_quotation} - KS X 1001 : {Convertor.convert_to_ksx1001_hex(name_quotation)}")
    print(f"ABC - UTF-16 : {Convertor.convert_to_utf16_be_hex('ABC')}")
    print(f"abc - UTF-16 : {Convertor.convert_to_utf16_be_hex('abc')}")
    print(f"가나다 - UTF-16 : {Convertor.convert_to_utf16_be_hex('가나다')}")
    print(f"각난닫 - UTF-16 : {Convertor.convert_to_utf16_be_hex('각난닫')}")
    print(f"{name_quotation} - UTF-16 : {Convertor.convert_to_utf16_be_hex(name_quotation)}")
    print(f"ABC - UTF-8 : {Convertor.convert_to_utf8_hex('ABC')}")
    print(f"abc - UTF-8 : {Convertor.convert_to_utf8_hex('abc')}")
    print(f"가나다 - UTF-8 : {Convertor.convert_to_utf8_hex('가나다')}")
    print(f"각난닫 - UTF-8 : {Convertor.convert_to_utf8_hex('각난닫')}")
    print(f"{name_quotation} - UTF-8 : {Convertor.convert_to_utf8_hex(name_quotation)}")

