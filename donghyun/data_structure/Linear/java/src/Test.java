import net.devgrus.util.ArrayList;
import net.devgrus.util.Collection;
import net.devgrus.util.LinkedList;

/**
 * Description
 * Donghyun Seo (egaoneko@naver.com)
 * 2014-12-05
 * Copyright ⓒ 2013-2014 Donghyun Seo All rights reserved.
 * version
 */
public class Test {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        LinkedList<Integer> list1 = new LinkedList<Integer>();
        LinkedList<Integer> list2 = new LinkedList<Integer>();

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

//        for (int i = 0; i < list.size(); i++) System.out.println(list.get(i));

        list.remove(2);

//        for (int i = 0; i < list.size(); i++) System.out.println(list.get(i));

        list1.add(1);
        list1.add(1);
        list1.add(2);
        list1.add(2);
        list1.add(3);
        list1.add(3);
        list1.add(4);
        list1.add(5);

//        list1.removeAll(list);
        list1.retainAll(list);

        for (int i = 0; i < list1.size(); i++) System.out.println(list1.get(i));


    }
}
