package net.devgrus.util;

import java.util.Iterator;
import java.lang.Object;

/**
 * <p><b>Collection Interface</b></p>
 * @author <a href="mailto:egaoneko@naver.com">Donghyun Seo</a>
 * <p>2014-11-30</p>
 * <p>Copyright ⓒ 2013-2014 Donghyun Seo All rights reserved.</p>
 * @version 1.0
 * @see java.util.Collection
 * 함수에 대한 설명은 <a href="http://book.naver.com/bookdb/book_detail.nhn?bid=6232200">자바의 정석</a>에서 참고하였다.
 */
public interface Collection<E> {

    /**
     * 지정된 객체(o)를 Collection 에 추가한다.
     * @param o 추가할 객체
     * @return  이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean add(E o);

    /**
     * 지정된 Collection(c) 의 객체들을 Collection 에 추가한다.
     * @param c 추가할 Collection 의 객체들
     * @return  이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean addAll(Collection<? extends E> c);

    /**
     * Collection 의 모든 객체를 삭제한다.
     */
    void clear();

    /**
     * 지정된 객체(o)를 Collection 에 포함되어 있는지 확인한다.
     * @param o 포함되어 있는지 확인할 객체
     * @return  지정된 객체가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean contains(Object o);

    /**
     * 지정된 Collection 의 객체들이 Collection 에 포함되어 있는지 확인한다.
     * @param c 포함되어 있는지 확인할 Collection 의 객체들
     * @return  지정된 Collection 의 객체들이 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean containsAll(Collection<?> c);

    /**
     * 동일한 Collection 인지 비교한다.
     * @param o 비교할 Collection
     * @return  비교할 Collection 이 동일하면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean equals(Object o);

    /**
     * Collection 이 비어있는지 확인한다.
     * @return  Collection 이 비어있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean isEmpty();

    /**
     * 지정된 객체를 삭제한다.
     * @param o Collection 안에 있다면 삭제할 객체
     * @return  이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean remove(Object o);

    /**
     * 지정된 Collection 에 포함된 객체들을 삭제한다.
     * @param c 이 Collection 에서 삭제할 객체들이 포함된 Collection
     * @return  이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean removeAll(Collection<?> c);

    /**
     * 지정된 Collection 에 포함된 객체들만을 남기고 다른 객체들은 Collection 에서 삭제한다.
     * 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     * @param c 이 Collection 에서 남길 객체들이 포함된 Collection
     * @return  이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    boolean retainAll(Collection<?> c);

    /**
     * Collection 에 저장된 객체의 개수를 반환한다.
     * @return  이 Collection 에 저장된 객체들의 개수
     */
    int size();

    /**
     * Collection 에 저장된 객체를 객체배열(Object[])로 반환한다.
     * @return  Collection 에 저장된 객체를 반환한 객체배열(Object[])
     */
    Object[] toArray();

    /**
     * 지정된 배열에 Collection 의 객체를 저장해서 반환한다.
     * @param a Collection 의 객체를 저장해서 반환할 객체배열(<T>T[])
     * @return  Collection 의 객체를 저장해서 반환한 객체배열(<T>T[])
     */
    <T> T[] toArray(T[] a);
}
