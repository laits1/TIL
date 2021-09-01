# SQL





##### 사원 테이블의 전체 목록을 출력

```SQL
SELECT * FROM EMP;
```

##### Line/Page size 변경

```SQL
set linesize 100; set pagesize 20;
```

##### Alias (별칭)

```sql
SELECT ENAME AS "별칭" FROM EMP;
```

##### 테이블 구조 확인

```sql
DESC {EMP}; 
DESCRIBE {EMP};
```

##### 문자열 연결

```sql
STRING || STRING
```

##### 사원 테이블의 모든 데이터를 출력

```sql
SELECT * FROM EMP;
```

##### 사원테이블에서 사원의 이름, 사원번호, 월급 출력

```sql
SELECT ENAME, EMPNO, SAL
FROM EMP;
```

##### 사원테이블에서 사원의 이름과 연봉을 출력

```sql
SELECT ENAME, SAL*12
FROM EMP;
```

##### 사원 테이블에서 사원의 이름, 입사일(HIREDATE), 부서번호(DEPTNO)를 출력하자

```SQL
SELECT ENAME, HIREDATE, DEPTNO
FROM EMP;
```

##### 사원 테이블에서 사원의 이름과, 해당 사원의 관리자(MGR)를 출력하자

```SQL
SELECT ENAME, MGR
FROM EMP;
```

##### 부서 테이블(DEPT)의 구조를 보자

```SQL
DESC DEPT;
```

##### 사원 테이블에서 사원의 이름, 월급, 커미션(COMM)을 출력하자

```SQL
SELECT ENAME, SAL, COMM
FROM EMP;
```

##### 사원 테이블의 모든 데이터를 “ㅇㅇ님이 ㅇㅇ에 입사를 하고 ㅇㅇ의 월급을 받습니다” 형식으로 출력하자

```SQL
SELECT ENAME || '님이 ' || HIREDATE || '에 입사를 하고 ' || SAL || '의 월급을 받습니다.' AS A
FROM EMP;
```

##### 사원 테이블에서 사원번호가 ‘7844’인 사원의 사원번호, 이름, 월급을 출력하자

```SQL
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE EMPNO = 7844;
```

##### 사원 테이블에서 ‘SMITH’의 사원번호, 이름, 월급을 출력하자

```SQL
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE ENAME = 'SMITH';
```

##### 사원 테이블에서 입사일이 1980년 12월 17일인 사원의 모든 데이터를 출력하자

```SQL
SELECT *
FROM EMP
WHERE HIREDATE = '1980/12/17';
```

##### 사원 테이블에서 1980년부터 1982년 사이에 입사한 사원의 이름과 입사일을 출력하자

```SQL
SELECT ENAME, HIRDATAE
FROM EMP
WHERE HIDRATE BTEWEEN '1980/01/01' AND '1982/12/31';
```

##### 월급이 2000 이하인 사원의 이름과 월급을 출력하자

```SQL
SELECT ENAME, SAL
FROM EMP
WHERE SAL <= 2000;
```

##### 사원번호가 7369, 7499, 7521인 사원들의 이름과 월급을 출력하자

```SQL
SELECT ENAME, SAL
FROM EMP
WHERE EMPNO IN (7369,7499,7521);
```



































#### 사원 테이블과 부서 테이블에서 사원들의 이름, 부서번호, 부서이름을 출력하자

```sql
SELECT E.ENAME, E.DEPTNO, D.DNAME
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO;
```

#### 사원 테이블과 부서 테이블에서 ‘DALLAS’ 에서 근무하는 사원의 이름, 직업, 부서번호, 부서이름을 출력하자

```sql
SELECT E.ENAME, E.JOB, E.DEPTNO, D.DNAME
FROM EMP E INNER JOIN DEPT D
ON E.DEPTNO = D.DEPTNO
WHERE D.LOC = 'DALLAS';

```

#### 사원 테이블과 부서 테이블에서 이름에 ‘A’ 가 들어가는 사원들의 이름과 부서이름을 출력하자
```sql
SELECT E.ENAME, D.DNAME
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO
AND E.ENAME LIKE '%A%';

```

#### 사원 테이블과 부서 테이블에서 사원의 이름과 부서의 이름, 월급을 출력하자 (월급이 3000 이산인 사원들만 출력하자)
```sql
SELECT E.ENAME, D.DNAME, E.SAL
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO
AND E.SAL >= 3000;
```

#### 사원 테이블과 부서 테이블에서 직업이 ‘SALESMAN’인 사원들의 직업과 사원 이름, 부서이름을 출력하자
```sql
SELECT E.JOB, E.ENAME, D.DNAME
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO
AND E.JOB = 'SALESMAN';
```

#### 사원 테이블과 급여 테이블(SALGRADE)에서 커미션이 책정된 사원들의 사원번호, 이름, 연봉, 연봉+커미션, 급여등급(GRADE)을 출력하자
(각각의 컬럼명을 ‘사원번호’, ‘사원이름’, ‘연봉’, ‘연봉2’, ‘급여등급’으로)
```sql
SELECT E.EMPNO 사원번호, E.ENAME 사원이름, E.SAL*12 연봉,(E.SAL * 12) + E.COMM 연봉2, S.GRADE S
FROM EMP E, SALGRADE S
WHERE E.SAL BETWEEN S.LOSAL AND S.HISAL
AND E.COMM > 0;
```

#### 사원 테이블과 부서 테이블, 급여 테이블에서 부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름, 월급, 급여등급을 출력하자
(부서번호가 낮은 순으로, 월급이 높은 순으로 출력하자)
```sql
SELECT D.DEPTNO, D.DNAME, E.ENAME, E.SAL, S.GRADE
FROM EMP E, DEPT D, SALGRADE S
WHERE E.DEPTNO = D.DEPTNO
AND E.SAL BETWEEN S.LOSAL AND S.HISAL
AND E.DEPTNO = 10
ORDER BY E.DEPTNO ASC, E.SAL DESC;

SELECT D.DEPTNO, D.DNAME, E.ENAME, E.SAL, S.GRADE
FROM EMP E 
INNER JOIN DEPT D ON (E.DEPTNO = D.DEPTNO)
INNER JOIN SALGRADE S ON (E.SAL >= S.LOSAL AND E.SAL <= S. HISAL)
WHERE D.DEPTNO = 10
ORDER BY E.DEPTNO ASC, E.SAL DESC;
```

#### 사원 테이블에서 사원번호와 사원이름, 관리자의 사원번호, 사원 이름을 출력하자
(각각의 컬럼명을 ‘사원번호’, ‘사원이름’, ‘관리자번호’, ‘관리자이름’으로)

```sql
SELECT E.EMPNO 사원번호, E.ENAME 사원이름, M.MGR 관리자번호, M.ENAME 관리자이름
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO;


SELECT
FROM E.

```

#### 사원 테이블과 부서 테이블에서 해당 부서의 모든 사원에 대한 부서이름, 위치, 사원수 및 평균 급여를 출력하자

```sql
SELECT DNAME, LOC, COUNT(*), AVG(SAL) 
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO
GROUP BY DNAME, LOC;


SELECT DNAME, LOC, COUNT(*), AVG(SAL) 
FROM EMP JOIN DEPT USING(DEPTNO)
GROUP BY DNAME, LOC;

```











