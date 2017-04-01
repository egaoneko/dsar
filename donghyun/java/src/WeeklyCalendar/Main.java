package WeeklyCalendar;

import java.io.FileInputStream;
import java.util.HashMap;
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
//        Scanner sc = new Scanner(new FileInputStream("src/WeeklyCalendar/input.txt"));

        Scanner sc = new Scanner(System.in);

        HashMap<String, Integer> map = new HashMap<>();
        map.put("Sunday", 0);
        map.put("Monday", 1);
        map.put("Tuesday", 2);
        map.put("Wednesday", 3);
        map.put("Thursday", 4);
        map.put("Friday", 5);
        map.put("Saturday", 6);

        int lastDay[] = {31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        T = sc.nextInt();
        for (test_case = 1; test_case <= T; test_case++) {
            //	이 부분에서 알고리즘 프로그램을 작성하십시오.

            int m = sc.nextInt();
            int d = sc.nextInt();
            String s = sc.next();

            int index = map.get(s);
//            int index = getIndex(s);

            int week[] = new int[7];

            for(int i = index; i >= 0; i--) {
                int day = d - (index - i);

                week[i] = day > 0? day : lastDay[m-1] + day;
            }

            for(int i = index + 1; i < 7; i++) {
                int day = d + (i - index);

                week[i] = day <= lastDay[m]? day : day - lastDay[m];
            }

            //	이 부분에서 정답을 출력하십시오.
            //  System.out.println("Case #" + test_case);

            for (int i : week) {
                System.out.print(i+" ");
            }
            System.out.println();
        }
    }

    public static int getIndex(String day) {

        switch (day) {
            case "Sunday":
                return 0;
            case "Monday":
                return 1;
            case "Tuesday":
                return 2;
            case "Wednesday":
                return 3;
            case "Thursday":
                return 4;
            case "Friday":
                return 5;
            case "Saturday":
                return 6;
            default:
                return -1;
        }
    }
}
