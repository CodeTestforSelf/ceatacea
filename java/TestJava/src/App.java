import java.util.Vector;

// 2023-01-18 객체지향 프로그래밍 언급하면서
public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, Java World!");

        String[] arr = {"AI", "Machine Learning", "Deep Learning", "Big Data"}; // 변수 선언&할당

        Vector<String> tmp = new Vector<String>(); // 객체 생성
        // 자바나 C++같은 언어에서는 동적으로 길이가 변하는 배열 벡터(Vector)를 제공한다. ref : https://erichika.tistory.com/56
        Vector<String> odd = new Vector<String>();
        // Java의 Generic 기능 -> 이 Vector에 문자열만 담겠다고 선언.

        for(int i = 0; i < arr.length; i++){
            tmp.add(arr[i]);
            if (i % 2 != 0){
                odd.add(arr[i]);
            }
        }
        System.out.println("tmp : "+tmp+" / size : "+tmp.size());
        System.out.println("odd : "+odd+" / size : "+odd.size());
    }
}

