// Q: http://www.hacker.org/challenge/chal.php?id=15
// A: http://www.hacker.org/challenge/chal.php?answer=-2147483648&id=15&go=Submit

public class RandomProblem {
	public int bucketFromRandom(int randomNumber) {
		int a[] = new int[10];
		for (int i = 0; i < a.length; i++)
			a[i] = i * randomNumber;
		int index = Math.abs(randomNumber) % a.length;
		return a[index];
	}

	public static void main(String[] args) {
		int randomNumber = Integer.MIN_VALUE;
		System.out.println(randomNumber);

		try {
			new RandomProblem().bucketFromRandom(randomNumber);
		} catch (Throwable t) {
			System.out.println(t);
		}
	}
}
