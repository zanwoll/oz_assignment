# 블록리스트 관리 파일

BLOCKLIST = set()

def add_to_blocklist(jtl):
    BLOCKLIST.add(jtl)

def remove_from_blocklist(jtl):
    BLOCKLIST.discard(jtl)