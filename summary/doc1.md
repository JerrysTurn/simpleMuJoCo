Intro
MuJoCo는 구글 딥마인드에 의해 2021년 무료로 사용라이센스가 풀리고 2022년에 오픈소스화 되었다.
C/C++을 기반으로 만들어진 시뮬레이터이며, MJCF scene description language를 사용한다. 

Generalized coordinates combined with modern contact dynamics
MuJoCo는 generalized coordinate 표현을 사용하며, optimization based contact dynamics를 풀었다.

일반적으로 컨택트 다이나믹스는 LCP or NCP 문제로 풀어가는데, 이를 convex optimization 문제로 축소시켜 계산을 진행하기 떄문에 계산 결과가 빠르다.

Tendon Geometry가 사용가능하다.

근데 MuJoCo documentation은 C 기준으로 작성되어있는 파트가 있다

Computation
일반적인 LCP 계산과 다른 과정이 존재한다.
## Tutorial
1. mjModel & mjData 간의 차이 확인 / OpenGL Rendering 방법

