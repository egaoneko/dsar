package net.devgrus.util;

/**
 * <p><b>List Interface</b></p>
 * @author <a href="mailto:egaoneko@naver.com">Donghyun Seo</a>
 * <p> 2014-12-01</p>
 * <p>Copyright ⓒ 2013-2014 Donghyun Seo All rights reserved.</p>
 * @version 1.0
 * @see java.util.List
 * 함수에 대한 설명은 <a href="http://book.naver.com/bookdb/book_detail.nhn?bid=6232200">자바의 정석</a>에서 참고하였다.
 */

public interface List<E> extends Collection<E> {

    /**
     * 지정된 위치(index)에 객체(element)를 추가한다.
     * @param index 지정할 위치
     * @param element   추가할 객체
     */
    void add(int index, E element);

    /**
     * 지정된 위치(index)에 컬렉션에 포함된 객체들을 추가한다.
     * @param index 지정할 위치
     * @param c 저장할 객체들이 포함된 Collection
     * @return  이 작업으로 인해 List 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean addAll(int index, Collection<? extends E> c);

    /**
     * 지정된 위치(index)에 있는 객체를 반환한다.
     * @param index 지정할 위치
     * @return  지정된 위치(index)에 있는 객체
     */
    E get(int index);

    /**
     * 지정된 객체의 위치(index)를 반환한다.
     * (List 의 첫 번째 요소부터 순방향으로 찾는다.)
     * @param o 지정할 객체
     * @return  지정된 객체의 List 의 첫 번째 요소부터 순방향으로 위치(index)
     */
    int indexOf(Object o);

    /**
     * 지정된 객체의 위치(index)를 반환한다.
     * (List 의 마지막 요소부터 역방향으로 찾는다.)
     * @param o 지정할 객체
     * @return  지정된 객체의 List 의 마지막 요소부터 역방향으로 위치(index)
     */
    int lastIndexOf(Object o);

    /**
     * 지정된 위치(index)에 있는 객체를 삭제하고 삭제된 객체를 반환한다.
     * @param index 지정할 위치
     * @return  지정된 위치(index)에 있었던 삭제된 객체
     */
    E remove(int index);

    /**
     * 지정된 위치(index)에 객체(element)를 저장한다.
     * @param index 지정할 위치
     * @param element   저장할 객체
     * @return  저장할 위치에 있었던 이전 객체
     */
    E set(int index, E element);

    /**
     * 지정된 범위(fromIndex 부터 toIndex)에 있는 객체를 반환한다.
     * @param fromIndex 지정할 시작 위치
     * @param toIndex   지정할 끝 위치
     * @return  지정된 범위(fromIndex 부터 toIndex)에 있는 객체
     */
    List<E> subList(int fromIndex, int toIndex);
}
