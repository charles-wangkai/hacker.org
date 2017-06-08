
// Q: http://www.hacker.org/challenge/chal.php?id=99
// A: http://www.hacker.org/challenge/chal.php?answer=383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027590099&id=99&go=Submit

// https://en.wikipedia.org/wiki/John_Machin

import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;

public class PrimalPi {
	static final int DIGIT_NUM = 2048;
	static final int SCALE = DIGIT_NUM + 5;
	static final BigDecimal ERROR = BigDecimal.valueOf(1, SCALE);
	static final int CERTAINTY = 10;

	public static void main(String[] args) {
		System.out.println(searchLongestPrime(computePiDigits()));
	}

	static String searchLongestPrime(String digits) {
		for (int length = digits.length();; length--) {
			for (int i = 0; i + length <= digits.length(); i++) {
				String part = digits.substring(i, i + length);
				if (new BigInteger(part).isProbablePrime(CERTAINTY)) {
					return part;
				}
			}
		}
	}

	static String computePiDigits() {
		BigDecimal pi = computeArctanForInverse(5).multiply(BigDecimal.valueOf(4))
				.subtract(computeArctanForInverse(239)).multiply(BigDecimal.valueOf(4));

		return pi.toString().substring(2, 2 + DIGIT_NUM);
	}

	static BigDecimal computeArctanForInverse(int denominator) {
		BigDecimal result = BigDecimal.ONE.divide(BigDecimal.valueOf(denominator), SCALE, RoundingMode.HALF_UP);

		BigDecimal factor = BigDecimal.valueOf(denominator * denominator);
		int divisor = 1;
		BigDecimal term = result;
		while (term.compareTo(ERROR) > 0) {
			divisor += 2;
			term = term.divide(factor, SCALE, RoundingMode.HALF_UP);
			result = result.subtract(term.divide(BigDecimal.valueOf(divisor), SCALE, RoundingMode.HALF_UP));

			divisor += 2;
			term = term.divide(factor, SCALE, RoundingMode.HALF_UP);
			result = result.add(term.divide(BigDecimal.valueOf(divisor), SCALE, RoundingMode.HALF_UP));
		}

		return result;
	}
}
