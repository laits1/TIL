# MONGODB

1. 설치
   - [MongoDB](https://www.mongodb.com/try/download/community) 에서 다운로드
     - 설치 중  Complete -> Next -> Install MongoDB Compass 체크 해제 -> Install
2. Path 설정
   - 시작 -> 고급 시스템 설정 -> 환경 변수 -> 시스템 변수 탭에서 Path 더블클릭 -> 새로 만들기 -> C:\Program Files\MongoDB\Server\5.0\bin 붙여넣기

3. 설치확인
   - CMD에서 mongo 



```mongo
function test(){
	print('test')
}

test()

function test2(n){
	return n + 10
}
test2(3)

var today = new Date();
today

show dbs
db

db.engineer.insertOne({"name":"신동엽"})
db.engineer.insertOne({"id":"kang","age":50})
db.engineer.find()

db.inventory.find( {item:"canvas"})
// inventory라는 collection에서
// item이라는 field 값이
// "canvas" 인 것을 찾아주세요


db.engineer.insertMany(
[
	{"name":"김선재", "취미":"차마시기"},
	{"name":"김민창", "주소":"고양시"},
	{"name":"황수빈", "고향":"인천시"},
	{"name":"안기용", "전화번호":"010-1122-3344"}

])

db.engineer.find({"name":"신동엽"})

// name 속성이 있는 documnets를 출력하자
db.engineer.find({"name":{$exists:true}})

// name 속성만 출력하자
db.engineer.find({}, {"name":1, "_id":0})

// id가 kang인 document를 찾아서 age를 55로 바꾸고싶다.
db.engineer.updateOne(
	{"id":"kang"},
	{$set:{"age":55}}
)
db.engineer.find()

db.engineer.replaceOne(
	{"id":{$exists:true}},
	{"name":"강호동"}
)

// name이 존재하는 documnets 들에
// class:engineer
db.engineer.updateMany(
{"name":{$exists:true}},
{$set:{"class":"engineer"}}
)

db.engineer.deleteOne({"name":{$exists:true}})

db.engineer.deleteMany({"name": {$exists:true}})

db.inventory.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])
```

