package Fixparen;

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
//        Scanner sc = new Scanner(new FileInputStream("src/Fixparen/input.txt"));

        Scanner sc = new Scanner(System.in);

        T = sc.nextInt();
        for (test_case = 1; test_case <= T; test_case++) {
            //	이 부분에서 알고리즘 프로그램을 작성하십시오.

            String s1 = sc.next();
            String s2 = sc.next();

            char[] list = s1.toCharArray();
            char[] lList = s2.toCharArray();
            char[] rList = getRList(lList);

            for (int i = 0; i < list.length; i++) {
                if (list.length % 2 != 0) {
                    return;
                }
                switch (list[i]) {
                    case '(':
                    case '{':
                    case '[':
                    case '<':
                        break;
                    case ')':
                    case '}':
                    case ']':
                    case '>':
                        int cnt = 1;
                        char l = 0;
                        int j = 0;

                        for (j = i-1; cnt != 0 || j < 0; j--) {
                            switch (list[j]) {
                                case '(':
                                case '{':
                                case '[':
                                case '<':
                                    cnt--;
                                    break;
                                case ')':
                                case '}':
                                case ']':
                                case '>':
                                    cnt++;
                                    break;
                            }
                            l = list[j];
                            if (j < 0) {
                                return;
                            } else if(cnt == 0) {
                                break;
                            }
                        }

                        char r = list[i];
                        int lRank = getRank(l, lList);
                        int rRank = getRank(r, rList);

                        if (lRank < rRank) {
                            list[i] = getBracket(l);
                        } else if(rRank < lRank) {
                            list[j] = getBracket(r);
                        }
                        break;
                }
            }

            //	이 부분에서 정답을 출력하십시오.
            //  System.out.println("Case #" + test_case);

            for (char c : list) {
                System.out.print(c);
            }
            System.out.println();
        }
    }

    public static char[] getRList(char[] lList) {
        char[] rList = new char[lList.length];

        for (int i = 0; i < lList.length; i++) {
            switch (lList[i]) {
                case '(':
                    rList[i] = ')';
                    break;
                case '{':
                    rList[i] = '}';
                    break;
                case '[':
                    rList[i] = ']';
                    break;
                case '<':
                    rList[i] = '>';
                    break;
            }
        }
        return rList;
    }

    public static int getRank(char s, char[] list) {
        for (int i = 0; i < list.length; i++) {
            if (list[i] == s) {
                return i;
            }
        }
        return -1;
    }

    public static char getBracket(char c) {
        switch (c) {
            case '(':
                return ')';
            case '{':
                return '}';
            case '[':
                return ']';
            case '<':
                return '>';
            case ')':
                return '(';
            case '}':
                return '{';
            case ']':
                return '[';
            case '>':
                return '<';
        }
        return (char)-1;
    }
}

