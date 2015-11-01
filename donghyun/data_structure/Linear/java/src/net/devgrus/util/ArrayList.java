package net.devgrus.util;

import java.util.NoSuchElementException;

/**
 * <p><b>ArrayList Class/b></p>
 * @author <a href="mailto:egaoneko@naver.com">Donghyun Seo</a>
 * <p>2014-12-05</p>
 * <p>Copyright ⓒ 2013-2014 Donghyun Seo All rights reserved.</p>
 * @version 1.0
 * @see java.util.ArrayList
 */

public class ArrayList<E> implements List<E>, Cloneable {

    /**
     * ArrayList 의 저장소인 배열
     */
    private Object[] elementData;

    /**
     * ArrayList 에 저장된 데이터의 수
     */
    private int size;

    /**
     * 현재 순회하고 있는 ArrayList 의 Index
     */
    private int curPosition;

    /**
     * ArrayList 에 저장된 데이터의 수
     */
    private int capacity;

    /**
     * ArrayList 의 빈 저장소 배열의 상수
     */
    private static final Object[] EMPTY_ELEMENTDATA = {};

    /**
     * ArrayList 의 기본 배열의 크기
     */
    private static final int DEFAULT_SIZE = 10;

    private  static  final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;

    /**
     * 모든 생성자에 공통으로 해당되는 부분의 초기화
     */
    {
        this.size = 0;
        this.curPosition = 0;
    }

    /**
     * ArrayList 의 크기를 지정하지 않았을 때의 생성자
     */
    public ArrayList() {
        this.elementData = new Object[DEFAULT_SIZE];
        this.capacity = DEFAULT_SIZE;
    }

    /**
     * ArrayList 의 크기를 지정하였을 때의 생성자
     * @param initialCapacity   지정할 ArrayList 의 크기
     */
    public ArrayList(int initialCapacity){
        if(initialCapacity > 0 ){
            this.elementData = new Object[initialCapacity];
            this.capacity = initialCapacity;
        } else if(initialCapacity == 0){
            this.elementData = EMPTY_ELEMENTDATA;
            capacity = 0;
        } else {
            throw new IllegalArgumentException("잘못된 배열의 크기 : "+initialCapacity);
        }

    }

    /**
     * 다른 Collection 을 인자로 주었을 때의 생성자
     * @param c 지정하고자 하는 Collection
     */
    public ArrayList(Collection<? extends E> c) {
        this.elementData = c.toArray();
        if ((this.size = this.elementData.length) != 0) {
            if (this.elementData.getClass() != Object[].class)
                this.elementData = java.util.Arrays.copyOf(this.elementData, this.size, Object[].class);
            this.capacity = this.size;
        } else {
            this.elementData = EMPTY_ELEMENTDATA;
            this.capacity = 0;
        }
    }

    /**
     * ArrayList 를 복사한 Instance 를 반환
     * @return  ArrayList 를 복사한 Instance
     */
    public Object clone() {
        try {
            ArrayList<?> v = (ArrayList<?>)super.clone();
            v.elementData = java.util.Arrays.copyOf(this.elementData, this.size);
            v.size = this.size;
            v.capacity = this.size;
            v.curPosition = 0;
            return v;
        } catch (CloneNotSupportedException e) {
            throw new InternalError(e);
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
        if(this.size >= MAX_ARRAY_SIZE) {
            throw new OutOfMemoryError();
        }

        if(this.size < this.capacity){
            this.elementData[size++] = o;
            return true;
        } else if(this.size >= this.capacity){
            expand();
            this.elementData[size++] = o;
            return true;
        }
        return false;
    }

    /**
     * ArrayList 의 크기를 확장
     */
    private void expand() {
        checkMaxSize(this.size);

        int oldCapacity = this.elementData.length;
        Object[] temp = this.elementData;
        this.elementData = new Object[oldCapacity+1];
        System.arraycopy(temp, 0, this.elementData, 0, temp.length);
        this.capacity ++;
    }

    /**
     * ArrayList 의 크기를 지정해서 확장
     * @param expandCapacity    확장할 크기
     */
    private void expand(int expandCapacity) {
        checkMaxSize(this.size+expandCapacity);

        int oldCapacity = this.elementData.length;
        Object[] temp = this.elementData;
        this.elementData = new Object[oldCapacity+expandCapacity];
        System.arraycopy(temp, 0, this.elementData, 0, temp.length);
        this.capacity += expandCapacity;
    }

    /**
     * ArrayList 의 크기가 정수 표현 범위를 넘는지 확인
     */
    private void checkMaxSize(int checkSize){
        if(checkSize >= MAX_ARRAY_SIZE) {
            throw new OutOfMemoryError();
        }
    }

    /**
     * 지정된 위치(index)에 객체(element)를 추가한다.
     *
     * @param index   지정할 위치
     * @param element 추가할 객체
     */
    @Override
    public void add(int index, E element) {
        checkMaxSize(this.size);

        if(index < 0){
            throw new IllegalArgumentException("잘못된 Index : "+index);
        }

        if(index > this.capacity - 1) {
            throw new IllegalArgumentException("잘못된 Index : "+index+" / ArrayList 의 크기 : "+this.capacity);
        }

        if(this.size >= this.capacity) {
            expand();
        }

        int moveSize = this.size-index;
        System.arraycopy(this.elementData, index, this.elementData, index + 1, moveSize);
        this.elementData[index] = element;
        size++;

        /*
        if(this.size < this.capacity){
            Object[] temp = elementData;
            this.elementData = new Object[this.elementData.length];
            if(index == 0) {
                this.elementData[index] = element;
                System.arraycopy(temp, 0, this.elementData, index+1, temp.length);
            }else {
                System.arraycopy(temp, 0, this.elementData, 0, index);
                this.elementData[index] = element;
                System.arraycopy(temp, index, this.elementData, index+1, this.size-index);
            }
            this.size++;
        } else if(this.size >= this.capacity){
            expand();
            Object[] temp = elementData;
            this.elementData = new Object[this.elementData.length];
            if(index == 0) {
                elementData[index] = element;
                System.arraycopy(temp, 0, this.elementData, index+1, temp.length);
            }else {
                System.arraycopy(temp, 0, this.elementData, 0, index);
                this.elementData[index] = element;
                System.arraycopy(temp, index, this.elementData, index+1, this.size-index);
            }
            this.size++;
        }
        */
    }

    /**
     * 지정된 Collection(c) 의 객체들을 Collection 에 추가한다.
     *
     * @param c 추가할 Collection 의 객체들
     * @return 이 작업으로 인해 Collection 에 변화가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean addAll(Collection<? extends E> c) {
        Object[] temp = c.toArray();
        int tempLen = temp.length;
        expand(tempLen);
        System.arraycopy(temp, 0, this.elementData, this.size, tempLen);
        this.size += tempLen;

        return tempLen != 0;
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
        Object[] temp = c.toArray();
        int tempLen = temp.length;
        expand(tempLen);

        int moveSize = this.size-index;
        if(index > 0){
            System.arraycopy(this.elementData, index, this.elementData, index+tempLen, moveSize);
        }
        System.arraycopy(temp, 0, this.elementData, index, tempLen);
        this.size += tempLen;

        return tempLen != 0;
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

        return elementData(index);
    }

    /**
     * 입력된 index 가 올바른지 검사한다.
     * @param index 입력한 index
     */
    private void checkRange(int index){
        if(index < 0 || index > size-1){
            throw new IllegalArgumentException("잘못된 Index : "+index);
        }
    }

    // index 를 이용하여 값을 구한다.
    E elementData(int index) {
        return (E)this.elementData[index];
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
        if(o == null){
            for (int i = 0; i < this.size; i++)
                if(this.elementData[i] == null) return i;
        }else{
            for (int i = 0; i < this.size; i++)
                if(o.equals(this.elementData[i])) return i;
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
        if(o == null){
            for (int i = this.size-1; i >= 0; i--)
                if(this.elementData[i] == null) return i;
        }else{
            for (int i = this.size-1; i >= 0; i--)
                if(o.equals(this.elementData[i])) return i;
        }
        return -1;
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
        E oldValue = elementData(index);

        int moveSize = this.size-index-1;
        if(moveSize > 0){
            System.arraycopy(this.elementData, index+1, this.elementData, index, moveSize);
        }
        elementData[--this.size] = null;

        return oldValue;
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

        E oldValue = elementData(index);
        elementData[index] = element;

        return oldValue;
    }

    /**
     * 지정된 범위(fromIndex 부터 toIndex)에 있는 객체를 반환한다.
     *
     * @param fromIndex 지정할 시작 위치
     * @param toIndex   지정할 끝 위치
     * @return 지정된 범위(fromIndex 부터 toIndex)에 있는 객체
     */
    @Override
    public List<E> subList(int fromIndex, int toIndex) {
        return null;
    }

    /**
     * Collection 의 모든 객체를 삭제한다.
     */
    @Override
    public void clear() {
        for (int i = 0; i < this.size; i++)
            this.elementData[i] = null;

        this.size = 0;
    }

    /**
     * 지정된 객체(o)를 Collection 에 포함되어 있는지 확인한다.
     *
     * @param o 포함되어 있는지 확인할 객체
     * @return 지정된 객체가 있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean contains(Object o) {
        /*
        for (int i = 0; i < this.size; i++)
            if(o.equals(this.elementData[i])) return true;
        return false;
        */
        return indexOf(o) >= 0;
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
     * Collection 이 비어있는지 확인한다.
     *
     * @return Collection 이 비어있으면 true 를 그렇지 않으면 false 를 반환한다.
     */
    @Override
    public boolean isEmpty() {
        return this.size == 0;
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
            for (int index = 0; index < this.size ; index++)
                if(this.elementData[index] == null) {
                    remove(index);
                    return true;
                }
        } else {
            for (int index = 0; index < this.size; index++)
                if (o.equals(this.elementData[index])) {
                    remove(index);
                    return true;
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
     * Collection 에 저장된 객체의 개수를 반환한다.
     *
     * @return 이 Collection 에 저장된 객체들의 개수
     */
    @Override
    public int size() {
        return size;
    }

    /**
     * Collection 에 저장된 객체를 객체배열(Object[])로 반환한다.
     *
     * @return Collection 에 저장된 객체를 반환한 객체배열(Object[])
     */
    @Override
    public Object[] toArray() {
        return java.util.Arrays.copyOf(elementData, size);
    }

    /**
     * 지정된 배열에 Collection 의 객체를 저장해서 반환한다.
     *
     * @param a Collection 의 객체를 저장해서 반환할 객체배열(<T>T[])
     * @return Collection 의 객체를 저장해서 반환한 객체배열(<T>T[])
     */
    @Override
    public <T>T[] toArray(T[] a) {
        if (a.length < this.size)
            return (T[]) java.util.Arrays.copyOf(this.elementData, size, a.getClass());
        System.arraycopy(elementData, 0, a, 0, size);
        if (a.length > size)
            a[size] = null;
        return a;
    }

    /**
     * ArrayList 의 순환시 다음 값이 있는지 확인한다.
     * @return  다음 값이 있다면 true, 다음 값이 없다면 false
     */
    public boolean hasRoundNext(){
        if(this.curPosition >= this.size -1){
            return false;
        }
        return true;
    }

    /**
     * ArrayList 의 순환시 순환자를 처음 값으로 설정하며 처음 값을 반환한다.
     * @return  처음 값
     */
    public E roundFirst(){
        this.curPosition = 0;

        return get(this.curPosition);
    }

    /**
     * ArrayList 의 순환시 다음 값을 가져온다.
     * @return  다음 값
     */
    public E roundNext(){
        if(!hasRoundNext()){
            throw new NoSuchElementException();
        }

        return get(this.curPosition++);
    }

    /**
     * ArrayList 의 내부 값을 출력해 보인다.
     */
    public void roundPrint(){
        System.out.print("[ ");
        for (int index = 0; index < this.size ; index++) {
            System.out.print(get(index));
            if(index < this.size-1) System.out.print(", ");
        }
        System.out.println("]");
    }

}
