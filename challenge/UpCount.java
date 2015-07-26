public class UpCount {
	// Original recursive method
	// private long calc(int depth) {
	// if (depth == 0)
	// return 1;
	// long cc = calc(depth - 1);
	// return cc + (depth % 7) + ((((cc ^ depth) % 4) == 0) ? 1 : 0);
	// }

	// Modified iterative method
	private long calcNonRecursive(int depth) {
		int result = 1;
		for (int i = 1; i <= depth; i++) {
			result = result + (i % 7) + ((((result ^ i) % 4) == 0) ? 1 : 0);
		}
		return result;
	}

	public static void main(String[] args) {
		UpCount uc = new UpCount();

		// Call the iterative method instead of the recursive to avoid
		// "java.lang.StackOverflowError"

		// System.out.println(uc.calc(11589));
		System.out.println(uc.calcNonRecursive(11589));
	}
}
