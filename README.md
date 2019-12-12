# SW_Contest
---
## 개요
2019년 SW Contest 출품작입니다.

## 팀
- 팀명 : 주차장 매니저
- 팀원 및 역할
  - 정영석 : [Keras](https://keras.io)를 사용한 차량 인식용 딥러닝 모델 구축
  - 박석주 : [FireBase](https://firebase.google.com/?gclid=CjwKCAiAxMLvBRBNEiwAKhr-nJnx6oenASpgqeAwGWb-DwlxMgEyUU4FBliOgdqjEIyl7XBcbx6KKBoCKJwQAvD_BwE)를 사용한 데이터베이스 구축, 영상 데이터 전처리
  - 류요선 : 안드로이드 어플리케이션 제작
  - 이연희 : 안드로이드 User Interface 보완, 보고서 및 포스터 제작
## 배경
- 최근 대기 질 향상 및 보행자의 안전을 위한 “차 없는 거리” 사업이 부상
- 대책이 마련되지 않은 채로 시행되고 있는 해당 사업은 주차 공간 부족과 같은 문제점을 야기하고 있다. 
- 한림대학교 역시 차 없는 거리를 조성하면서 기존에 주차장으로 사용되던 공간이 사라져 학생 및 교직원의 주차공간 문제가 하나의 이슈로 떠올랐다.

## 기능
- CCTV에서 찍힌 영상을 사용해 영상정보 획득
- CCTV의 영상을 기계학습 모델을 사용해 분석
- 차량의 주차여부를 판단한여 웹상의 데이터베이스에 해당 정보를 동기화
- 해당 정보를 동기화 한 후 모바일 어플리케이션을 통해 주차정보 제공
- 어플리케이션상 자신 차량의 위치정보 제공 가능
## 핵심 문서
| 파일명 | 파일 설명 |
|----|----|
| Parking lot/App/manifests | 어플리케이션의 퍼미션 및 각종 기본설정 |
| Parking lot/App/java/com.example.parkinglot | 어플리케이션의 각 엑티비티별 java 소스 모음 |
| Parking lot/App/res/anim | 각종 애니메이션 효과 xml파일 |
| Firebase/firebase.py | FireBase 실행을 위한 파일 |
| Car detection Model/data_preprocessing.py | 모델 입력 전 전처리를 위한 모델 |
| Car detection Model/make_model.py | 모델 정의 |
| Car detection Model/train_model.py | 모델 훈련 |
| Car detection Model/predict_model | 값 예측 후 서버에 올림 |

## 디렉토리 구조
```
Parking lot 		안드로이드 관련 소스코드
Car detection Model 	차량 인식을 위한 모델
parking.mp4		실험에서 사용한 영상
FireBase			FireBase와 연동을 하기 위한 함수정의
```

