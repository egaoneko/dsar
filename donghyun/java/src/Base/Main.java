package Base;

import java.io.FileInputStream;
import java.util.Scanner;

/* 사용하는 클래스명이 Main 이어야 하며, 가급적 Main.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Main 명령으로 프로그램을 수행해 볼 수 있습니다. */

class Main {
    public static void main(String args[]) throws Exception {
        int T;
        int test_case;
        /* 아래 메소드 호출은 앞으로 표준 입력(키보드) 대신 input.txt 파일로 부터 읽어오겠다는 의미의 코드입니다.
           만약 본인의 PC 에서 테스트 할 때는, 입력값을 input.txt에 저장한 후 이 코드를 첫 부분에 추가하면,
           그 아래에서 입력을 수행할 때 표준 입력 대신 input.txt 파일로 부터 입력값을 읽어 올 수 있습니다.
           따라서 본인의 PC 에서 테스트 할 때에는 아래 주석을 지우고 이 메소드를 사용하셔도 됩니다.
           단, 이 시스템에서 "제출하기" 할 때에는 반드시 이 메소드를 지우거나 주석 처리 하셔야 합니다. */
        Scanner sc = new Scanner(new FileInputStream("src/Base/input.txt"));

//        Scanner sc = new Scanner(System.in);

        T = sc.nextInt();
        for (test_case = 1; test_case <= T; test_case++) {
            //	이 부분에서 알고리즘 프로그램을 작성하십시오.

            int N = sc.nextInt();
            String S = sc.next();

            //	이 부분에서 정답을 출력하십시오.
            //  System.out.println("Case #" + test_case);
        }
    }
}
