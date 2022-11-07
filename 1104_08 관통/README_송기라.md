1. 학습한 내용
  - base.html에 script를 가져와도 
  - 비동기 통신기능을 axios를 적용할시 각 html에 따로 axios script 적용 태그<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>를 추가해야함 base파일에 통으로 넣으면 적용 안됨.
  - 태그에서 id 속성을 추가하고 axios를 적용하면 action과 method를 삭제해도 됨. querySelector를 통해 지정하고   addEventListener 을 통해 post과 url 적용
  - then 
2. 어려웠던 부분
  - 팔로잉과 리뷰 좋아요 기능에서 숫자를 실시간 적용시킬때 views에서 query문으로 변수를 만들고 axios에서 지정한 태그로 변수를 넣어야 했음.
3. 새로 배운 것들 및 느낀점
  - 배운대로 따라하는데 자동완성 기능 지원이 안되다보니 오타로 인해 오류 나는 경우가 빈번해서 주의해야함.

= 구현 알고리즘
popularity와 vote_average 높은 순을 기준으로 10개 가져오기