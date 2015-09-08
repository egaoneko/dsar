package net.devgrus.util;

import java.util.NoSuchElementException;

/**
 * <p><b>ArrayList Class/b></p>
 * @author <a href="mailto:egaoneko@naver.com">Donghyun Seo</a>
 * <p> 2014-12-13</p>
 * <p>Copyright ⓒ 2013-2014 Donghyun Seo All rights reserved.</p>
 * @version 1.0
 * @see java.util.LinkedList
 */
public class LinkedList<E> implements List<E>, Cloneable {

    /**
     * LinkedList 에 저장된 데이터의 수
     */
    private int size;

    /**
     * LinkedList 의 첫 번째 Node
     */
    private Node<E> first;  // Head

    /**
     * LinkedList 의 마지막 Node
     */
    private Node<E> last;   // Tail

    {
        this.size = 0;
    }

    /**
     * 빈 생성자
     */
    public LinkedList() {

    }

    /**
     * 다른 Collection 을 인자로 주었을 때의 생성자
     * @param c 지정하고자 하는 Collection
     */
    public LinkedList(Collection<? extends E> c){
        this();
        addAll(c);
    }

    /**
     * Index 위치의 Node
     * @param index
     * @return
     */
    Node<E> node(int index) {
        // LinkedList 의 크기의 절반을 기준으로 작으면 처음부터, 크면 마지막부터 찾는다.
        if (index < (size >> 1)) {
            Node<E> x = first;
            for (int i = 0; i < index; i++) // 처음부터 index 번째까지 이동한다.
                x = x.next;
            return x;
        } else {
            Node<E> x = last;
            for (int i = size - 1; i > index; i--)  // 끝부터 index 번째까지 이동한다.
                x = x.prev;
            return x;
        }
    }

    /**
     * LinkedList 의 첫 번째에 추가한다.
     * @param e 추가할 요소
     */
    private void linkFirst(E e){
        final Node<E> f = first;
        final Node<E> newNode = new Node<E> (null, e, f);

        first = newNode;
        if(f == null)
            last = newNode;
        else
            f.prev = newNode;
        size++;
    }

    /**
     *  LinkedList 의 마지막에 추가한다.
     * @param e 추가할 요소
     */
    private void linkLast(E e){
        final Node<E> l = last;
        final Node<E> newNode = new Node<E> (l, e, null);

        last = newNode;
        if(l == null)
            first = newNode;
        else
            l .next = newNode;
        size++;
    }

    /**
     * LinkedList 의 이미 존재하는 요소 앞에 요소를 추가할 때
     * @param e 추가할 요소
     * @param succ  추가할 요소를 앞에 추가할 이미 존재하는 요소
     */
    private void linkBefore(E e, Node<E> succ) {
        // assert succ != null;
        final Node<E> pred = succ.prev;
        final Node<E> newNode = new Node<E>(pred, e, succ);

        succ.prev = newNode;
        if(pred == null)
            first = newNode;
        else
            pred.next = newNode;
        size++;
    }

    /**
     * LinkedList 의 첫 번째 요소를 제거한다.
     * @param f LinkedList 의 첫 번째 요소
     * @return  삭제된 요소의 값
     */
    private E unlinkFirst(Node<E> f){
        // assert f == first && f != null;
        final E element = f.item;
        final Node<E> next = f.next;

        /* GC */
        f.item = null;
        f.next = null;

        first = next;
        if (next == null)
            last = null;
        else
            next.prev = null;
        size--;

        return element;
    }

    /**
     * LinkedList 의 마지막 요소를 제거한다.
     * @param l LinkedList 의 마지막 요소
     * @return  삭제된 요소의 값
     */
    private E unlinkLast(Node<E> l) {
        // assert l == last && l != null;
        final E element = l.item;
        final Node<E> prev = l.prev;

        /* GC */
        l.item = null;
        l.prev = null;

        last = prev;
        if (prev == null)
            first = null;
        else
            prev.next = null;
        size--;

        return element;
    }

    /**
     * LinkedList 의 특정 요소를 제거한다.
     * @param x 제거할 요소
     * @return  삭제된 요소의 값
     */
    E unlink(Node<E> x) {
        // assert x != null;
        final E element = x.item;
        final Node<E> next = x.next;
        final Node<E> prev = x.prev;

        if (prev == null) {
            first = next;
        } else {
            prev.next = next;
            x.prev = null;
        }

        if (next == null) {
            last = prev;
        } else {
            next.prev = prev;
            x.next = null;
        }

        x.item = null;
        size--;

        return element;
    }

    /**
     * 지정된 위치(index)에 객체(element)를 추가한다.
     *
     * @param index   지정할 위치
     * @param element 추가할 객체
     */
    @Override
    public void add(int index, E element) {
        checkRange(index);

        if(index == size)
            linkLast(element);
        else
            linkBefore(element, node(index));

    }

    /**
     * 입력된 index 가 올바른지 검사한다.
     * @param index 입력한 index
     */
    private void checkRange(int index){
        if(index < 0 || index > size){
            throw new IllegalArgumentException("잘못된 Index : "+index);
        }
    }

    /**
     * 지정된 객체(o)를 Collection 에 추가한다.
     *
     * @param o 추가할 객체
     * @return 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean add(E o) {
        linkLast(o);
        return true;
    }

    /**
     * 지정된 위치(index)에 컬렉션에 포함된 객체들을 추가한다.
     *
     * @param index 지정할 위치
     * @param c     저장할 객체들이 포함된 Collection
     * @return 이 작업으로 인해 List 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean addAll(int index, Collection<? extends E> c) {
        checkRange(index);

        Object[] a = c.toArray();
        int numNew = a.length;
        if (numNew == 0)
            return false;

        Node<E> pred, succ;
        if (index == size) {
            succ = null;
            pred = last;
        } else {
            succ = node(index);
            pred = succ.prev;
        }

        for (Object o : a) {
            @SuppressWarnings("unchecked") E e = (E) o;
            Node<E> newNode = new Node<E>(pred, e, null);
            if (pred == null)
                first = newNode;
            else
                pred.next = newNode;
            pred = newNode;
        }

        if (succ == null) {
            last = pred;
        } else {
            pred.next = succ;
            succ.prev = pred;
        }

        size += numNew;
        return true;
    }

    /**
     * 지정된 Collection(c) 의 객체들을 Collection 에 추가한다.
     *
     * @param c 추가할 Collection 의 객체들
     * @return 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean addAll(Collection<? extends E> c) {
        return addAll(size, c);
    }

    /**
     * 객체(o)를 LinkedList 의 첫 번째 요소 앞에 추가한다.
     * @param o 첫 번째 요소 앞에 추가할 객체
     */
    public void addFirst(E o){
        linkFirst(o);
    }

    /**
     * 객체(o)를 LinkedList 의 마지막 요소 뒤에 추가한다.
     * @param o 마지막 요소 뒤에 추가할 객체
     */
    public void addLast(E o){
        linkLast(o);
    }

    /**
     * 지정된 위치(index)에 있는 객체를 반환한다.
     *
     * @param index 지정할 위치
     * @return 지정된 위치(index)에 있는 객체
     */
    @Override
    public E get(int index) {
        checkRange(index);
        return node(index).item;
    }

    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * @return  LinkedList 의 첫 번째 요소
     */
    public E getFist(){
        final Node<E> f = first;
        if(f == null)
            throw new NoSuchElementException();
        return f.item;  // final 로 선언된 변수의 내부 변수는 변경이 가능하다.
    }

    /**
     * LinkedList 의 마지막 요소를 반환한다.
     * @return  LinkedList 의 마지막 요소
     */
    public E getLast(){
        final Node<E> l = last;
        if(l == null)
            throw new NoSuchElementException();
        return l.item;
    }

    /**
     * 지정된 위치(index)에 객체(element)를 저장한다.
     *
     * @param index   지정할 위치
     * @param element 저장할 객체
     * @return 저장할 위치에 있었던 이전 객체
     */
    @Override
    public E set(int index, E element) {
        checkRange(index);
        Node<E> x = node(index);
        E oldVal = x.item;
        x.item = element;
        return oldVal;
    }

    /**
     * 지정된 위치(index)에 있는 객체를 삭제하고 삭제된 객체를 반환한다.
     *
     * @param index 지정할 위치
     * @return 지정된 위치(index)에 있었던 삭제된 객체
     */
    @Override
    public E remove(int index) {
        checkRange(index);
        return unlink(node(index));
    }

    /**
     * 지정된 객체를 삭제한다.
     *
     * @param o Collection 안에 있다면 삭제할 객체
     * @return 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean remove(Object o) {
        if(o == null){
            for(Node<E> x = first; x != null; x = x.next){
                if(x.item == null){
                    unlink(x);
                    return true;
                }
            }
        } else {
            for (Node<E> x = first; x != null ; x = x.next){
                if(o.equals(x.item)){
                    unlink(x);
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * 지정된 Collection 에 포함된 객체들을 삭제한다.
     *
     * @param c 이 Collection 에서 삭제할 객체들이 포함된 Collection
     * @return 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean removeAll(Collection<?> c) {
        Boolean ret = false;
        Object[] temp = c.toArray();

        if(temp.length == 0) return ret;

        for (int index = 0; index < temp.length; index++)
            while (remove(temp[index])) ret = true;

        return ret;
    }

    /**
     * LinkedList 의 첫 번째 요소를 제거한다.
     * @return  제거한 첫 번째 요소
     */
    public E removeFirst(){
        final Node<E> f = first;
        if(f == null)
            throw new NoSuchElementException();
        return unlinkFirst(f);
    }

    /**
     * LinkedList 의 마지막 요소를 제거한다.
     * @return  제거한 마지막 요소
     */
    public E removeLast(){
        final Node<E> l = last;
        if(l == null)
            throw new NoSuchElementException();
        return unlinkLast(l);
    }

    /**
     * 지정된 객체의 위치(index)를 반환한다.
     * (List 의 첫 번째 요소부터 순방향으로 찾는다.)
     *
     * @param o 지정할 객체
     * @return 지정된 객체의 List 의 첫 번째 요소부터 순방향으로 위치(index)
     */
    @Override
    public int indexOf(Object o) {
        int index = 0;
        if (o == null) {
            for (Node<E> x = first; x != null; x = x.next) {
                if (x.item == null)
                    return index;
                index++;
            }
        } else {
            for (Node<E> x = first; x != null; x = x.next) {
                if (o.equals(x.item))
                    return index;
                index++;
            }
        }
        return -1;
    }

    /**
     * 지정된 객체의 위치(index)를 반환한다.
     * (List 의 마지막 요소부터 역방향으로 찾는다.)
     *
     * @param o 지정할 객체
     * @return 지정된 객체의 List 의 마지막 요소부터 역방향으로 위치(index)
     */
    @Override
    public int lastIndexOf(Object o) {
        int index = size;
        if (o == null) {
            for (Node<E> x = last; x != null; x = x.prev) {
                index--;
                if (x.item == null)
                    return index;
            }
        } else {
            for (Node<E> x = last; x != null; x = x.prev) {
                index--;
                if (o.equals(x.item))
                    return index;
            }
        }
        return -1;
    }

    /**
     * 지정된 범위(fromIndex 부터 toIndex)에 있는 객체를 반환한다.
     *
     * @param fromIndex 지정할 시작 위치
     * @param toIndex   지정할 끝 위치
     * @return 지정된 범위(fromIndex 부터 toIndex)에 있는 객체
     */
    @Override
    public List<E> subList(int fromIndex, int toIndex) { return null; }

    /**
     * Collection 의 모든 객체를 삭제한다.
     */
    @Override
    public void clear() {
        for (Node<E> x = first; x != null; ) {
            Node<E> next = x.next;
            x.item = null;
            x.next = null;
            x.prev = null;
            x = next;
        }
        first = last = null;
        size = 0;
    }

    /**
     * 지정된 객체(o)를 Collection 에 포함되어 있는지 확인한다.
     *
     * @param o 포함되어 있는지 확인할 객체
     * @return 지정된 객체가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean contains(Object o) {
        return indexOf(o) != -1;
    }

    /**
     * 지정된 Collection 의 객체들이 Collection 에 포함되어 있는지 확인한다.
     *
     * @param c 포함되어 있는지 확인할 Collection 의 객체들
     * @return 지정된 Collection 의 객체들이 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean containsAll(Collection<?> c) {
        Object[] temp = c.toArray();

        if(temp.length == 0) return true;

        for (int index = 0; index < temp.length; index++) {
            if(!contains(temp[index])) return false;
        }

        return true;
    }

    /**
     * 지정된 Collection 에 포함된 객체들만을 남기고 다른 객체들은 Collection 에서 삭제한다.
     * 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     *
     * @param c 이 Collection 에서 남길 객체들이 포함된 Collection
     * @return 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean retainAll(Collection<?> c) {
        boolean ret = false;
        Object[] temp = toArray();

        for (int i = 0; i < temp.length; i++)
            if(!containsForRetainAll(c, temp[i])) {
                remove(temp[i]);
                ret = true;
            }

        return ret;
    }

    private boolean containsForRetainAll(Collection<?> c, Object o) {
        Object[] temp = c.toArray();

        for (int index = 0; index < temp.length; index++)
            if(o.equals(temp[index])) return true;

        return false;
    }

    /**
     * Collection 이 비어있는지 확인한다.
     *
     * @return Collection 이 비어있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean isEmpty() {
        return this.size == 0;
    }

    /**
     * Collection 에 저장된 객체의 개수를 반환한다.
     *
     * @return 이 Collection 에 저장된 객체들의 개수
     */
    @Override
    public int size() {
        return this.size;
    }

    /**
     * Collection 에 저장된 객체를 객체배열(Object[])로 반환한다.
     *
     * @return Collection 에 저장된 객체를 반환한 객체배열(Object[])
     */
    @Override
    public Object[] toArray() {
        Object[] result = new Object[size];
        int i = 0;
        for (Node<E> x = first; x != null; x = x.next)
            result[i++] = x.item;
        return result;
    }

    /**
     * 지정된 배열에 Collection 의 객체를 저장해서 반환한다.
     *
     * @param a Collection 의 객체를 저장해서 반환할 객체배열(<T>T[])
     * @return Collection 의 객체를 저장해서 반환한 객체배열(<T>T[])
     */
    @Override
    public <T> T[] toArray(T[] a) {
        if (a.length < size)
            a = (T[])java.lang.reflect.Array.newInstance(
                    a.getClass().getComponentType(), size);
        int i = 0;
        Object[] result = a;
        for (Node<E> x = first; x != null; x = x.next)
            result[i++] = x.item;

        if (a.length > size)
            a[size] = null;

        return a;
    }

    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * @return  LinkedList 의 첫 번째 요소
     */
    public E element() {
        return getFist();
    }

    /**
     * 지정된 객체(o)를 LinkedList 의 끝에 추가한다.
     * 저장에 성공하면 true, 실패하면 false 를 반환한다.
     * @param o 지정할 객체
     * @return  저장에 성공하면 true, 실패하면 false 를 반환
     */
    public boolean offer(E o){
        return add(o);
    }

    /**
     * 지정된 객체(o)를 LinkedList 의 처음에 추가한다.
     * 저장에 성공하면 true, 실패하면 false 를 반환한다.
     * @param o 지정할 객체
     * @return  저장에 성공하면 true, 실패하면 false 를 반환
     */
    public boolean offerFist(E o){
        addFirst(o);
        return true;
    }

    /**
     * 지정된 객체(o)를 LinkedList 의 끝에 추가한다.
     * 저장에 성공하면 true, 실패하면 false 를 반환한다.
     * @param o 지정할 객체
     * @return  저장에 성공하면 true, 실패하면 false 를 반환
     */
    public boolean offerLast(E o){
        addLast(o);
        return true;
    }

    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * @return  LinkedList 의 첫 번째 요소
     */
    public E peek(){
        final Node<E> f = first;
        return (f == null) ? null : f.item;
    }

    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * @return  LinkedList 의 첫 번째 요소
     */
    public E peekFirst(){
        final Node<E> f = first;
        return (f == null) ? null : f.item;
    }

    /**
     * LinkedList 의 마지막 요소를 반환한다.
     * @return  LinkedList 의 마지막 요소
     */
    public E peekLast(){
        final Node<E> l = last;
        return (l == null) ? null : l.item;
    }


    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * LinkedList 에서는 제거된다.
      * @return LinkedList 의 첫 번째 요소
     */
    public E poll(){
        final Node<E> f = first;
        return (f == null) ? null : unlinkFirst(f);
    }

    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * LinkedList 에서는 제거된다.
     * @return LinkedList 의 첫 번째 요소
     */
    public E pollFirst(){
        final Node<E> f = first;
        return (f == null) ? null : unlinkFirst(f);
    }

    /**
     * LinkedList 의 마지막 요소를 반환한다.
     * LinkedList 에서는 제거된다.
     * @return LinkedList 의 마지막 요소
     */
    public E pollLast(){
        final Node<E> l = last;
        return (l == null) ? null : unlinkLast(l);
    }

    /**
     * 지정된 객체(o)를 LinkedList 의 처음에 추가한다.
     * @param o 지정할 객체
     */
    public void push(E o){
        addFirst(o);
    }

    /**
     * LinkedList 의 첫 번째 요소를 반환한다.
     * LinkedList 에서는 제거된다.
     * @return LinkedList 의 첫 번째 요소
     */
    public E pop(){
        return removeFirst();
    }

    /**
     * LinkedList 에서 사용할 Node 내부 클래스
     * @param <E>   저장할 객체
     */
    private static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E item, Node<E> next){
            this.item = item;
            this.next = next;
            this.prev = prev;
        }
    }
}
