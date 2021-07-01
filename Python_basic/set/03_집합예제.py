PartyA = {"Park", "Kim", "Lee"}
PartyB = {"Park", "길동", "몽룡"}

print(f"파티에 참석한 모든 사람 : {PartyA | PartyB}")
print(f"2개의 파티에 참석한 모든 사람 : {PartyA & PartyB}")
print(f"파티 A에만 참석한 사람 : {PartyA-PartyB}")
print(f"파티 B에만 참석한 사람 : {PartyB-PartyA}")
