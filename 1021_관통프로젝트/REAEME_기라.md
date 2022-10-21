1. 학습한 내용
- ModelForm과 Modelserializer 은 형태가 비슷
- postman을 활용하여 쉽게 코드에 오류가 발생하여도 빠르게 원인을 찾아 수정할수 있었습니다.
- rest_framework의 status를 통해 성공/실패를 하게되면 결과(201, 204, 404 등등)를 지정할수 있다.
- serializer를 만들고 is_valid()로 확인할때, raise_exception=True 옵션을 사용하게 되면 굳이 Response에서 status기능에 HTTP_400을 지정하지 않아도 404가 결과로 출력됨
- 'PUT' 수정기능에서 일부만 수정하고 반영하고 싶을때는 serializer 인스턴스를 만들때 ()안에  partial = True 옵션 추가
2. 어려웠던 부분
- actor_movies 중개모델 class로 만들지 않고 실행하기 위해 Actor, Movie, Review 순서를 바꿔가며 인스턴스를 만들었지만 실패하였고, 결국 class 형태를 갖추고 인스턴스를 만들어서 활용하였습니다.   
3. 새로 배운 것 및 느낀 점
- 역참조를 하는 법은 학습해서 알고습니다. 전체 세부정보가 아닌 일부정보만 첨가하기 위해 (너무 직관적이고 코드가 많이 늘어나게 되어서) class를 추가하지 않는 여러 방법을 찾아보았지만 결국 serializers class를 추가로 만들어내는 것이 가장 빠르고 쉬운 방법이라는 것을 알게되었습니다.
- 
