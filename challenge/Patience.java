// Q: http://www.hacker.org/challenge/chal.php?id=64
// A: http://www.hacker.org/challenge/chal.php?answer=9085560309849087808&id=64&go=Submit

// Download the file: http://www.hacker.org/challenge/misc/Branches.class
// Use a Java decompiler (JD-GUI: http://jd.benow.ca/) to see the source code of the Java class file.

import java.math.BigInteger;
import java.util.Random;

public class Patience {
	public static void main(String[] args) {
		Random paramArrayOfString = new Random(739391L);
		long l;
		String str;
		do {
			while ((l = paramArrayOfString.nextLong()) < 0L) {
			}

			// Original code
			// BigInteger localBigInteger1;
			// BigInteger localBigInteger2 = localBigInteger1 = new
			// BigInteger(Long.toString(l));
			// str = null;
			// for (int i = 0; i < 20000; i++) {
			// localBigInteger2 = localBigInteger1 = (localBigInteger1 =
			// localBigInteger1.add(localBigInteger2))
			// .add(new BigInteger("1"));
			// str = localBigInteger1.toString();
			// }

			// Added code
			BigInteger p = BigInteger.valueOf(2).modPow(BigInteger.valueOf(20000), BigInteger.valueOf(1000000000));
			str = BigInteger.valueOf(l).multiply(p).add(p.subtract(BigInteger.ONE)).toString();

		} while (!(str = str.substring(str.length() - 9)).equals("843997183"));
		System.out.println(l);
	}
}