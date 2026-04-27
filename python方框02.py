# coding: utf-8
# ------------  仅新增 1 个工具函数  ------------
def box_print(*lines, padding=1):
    """终端单框，支持中文，0 依赖"""
    import unicodedata
    def disp_width(s: str) -> int:
        return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in s)
    lines = [str(l) for l in lines]
    w = max(disp_width(l) for l in lines) if lines else 0
    inner = w + padding * 2
    top, bot = '┌' + '─' * inner + '┐', '└' + '─' * inner + '┘'
    print(top)
    for ln in lines:
        sp, extra = ' ' * padding, w - disp_width(ln)
        print(f'│{sp}{ln}{" " * extra}{sp}│')
    print(bot)

# ------------  原有数据库  ------------
std_db = [
    {"id": 1, "name": "尾门铭牌", "path": "imp/1.jpg"},
    {"id": 3, "name": "尾门堵塞", "path": "imp/3.jpg"}
]

# ------------  原有工具函数  ------------
def exist_id(iid):          # 判断 id 是否存在
    return any(item['id'] == iid for item in std_db)

def add_record(iid, name, path):
    if not exist_id(iid):
        std_db.append({"id": iid, "name": name, "path": path})
        box_print(f"已添加 → id={iid}  name={name}")   # ▶ 框住提示
    else:
        box_print(f"id {iid} 已存在，未添加。")        # ▶ 框住提示

def del_record(iid):
    for idx, item in enumerate(std_db):
        if item['id'] == iid:
            std_db.pop(idx)
            box_print(f"已删除 → id={iid}  name={item['name']}")  # ▶ 框住提示
            return
    box_print(f"id {iid} 不存在，无法删除。")                   # ▶ 框住提示

def list_all():
    if not std_db:
        box_print("（数据库为空）")
        return
    for item in std_db:
        box_print(f"id={item['id']}  |  name={item['name']}  |  path={item['path']}")

# ------------  交互主循环  ------------
def main():
    list_all()                      # 启动时先打印现有数据
    while True:
        try:
            cmd = input("\n命令(add id name path  /  del id  /  list  /  quit): ").strip()
            if not cmd:
                continue
            parts = cmd.split()
            op = parts[0].lower()

            if op == 'add' and len(parts) == 4:
                _, iid, name, path = parts
                add_record(int(iid), name, path)

            elif op == 'del' and len(parts) == 2:
                del_record(int(parts[1]))

            elif op == 'list':
                list_all()

            elif op == 'quit':
                box_print("拜拜~")
                break
            else:
                box_print("格式错误！\n用法：\n  add id name path\n  del id\n  list\n  quit")
        except ValueError:
            box_print("id 必须是整数！")
        except KeyboardInterrupt:
            box_print("用户中断，退出。")
            break

if __name__ == '__main__':
    main()
