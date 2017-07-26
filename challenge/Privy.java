
// Q: http://www.hacker.org/challenge/chal.php?id=16
// A: http://www.hacker.org/challenge/chal.php?answer=kuakua&id=16&go=Submit

// Download the file: http://www.hacker.org/challenge/misc/Privy.bin
// Find that the file begins with the Java class file magic number "0xCAFEBABE", so change the suffix from ".bin" to ".class".
// Use a Java decompiler (JD-GUI: http://jd.benow.ca/) to see the source code of the Java class file.

public class Privy {
	public void showMeSomethingBoring() {
		System.out.println("this is not interesting. look elsewhere.");
	}

	private void showMeSomethingInteresting() {
		char[] c = { 'a', 'x', 'k', 'y', 'u', 'e' };
		int a = 73;
		int b = 391;
		String s = "";
		for (int i = 0; i < 6; i++) {
			s = s + c[((i * b + (i + 8) * a) % c.length)];
		}
		System.out.println(s);
	}

	public static void main(String[] args) {
		// Original code
		// new Privy().showMeSomethingBoring();

		// Added code
		new Privy().showMeSomethingInteresting();
	}
}