/*
 * Assignment given by Marc Liberatore.
 *
 * Solution/code by: Xavier Wrenn
 */

package simulation;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * A Java class to simulate the card game War. See assignment writeup for
 * details.
 *
 */
public class War {
	ArrayList<Integer> player1AHand;
	ArrayList<Integer> player2BHand;
	ArrayList<Integer> deck;
	ArrayList<Integer> spoil;
	ArrayList<Integer> topCards;
	int battles;

	/**
	 * Determines the winner of a game of War, returning 1 if player A wins, -1 if
	 * player B wins, 0 if a draw.
	 *
	 * The rules of the game are defined in the assignment writeup.
	 *
	 * @param deck
	 * @return 1 if player A wins, -1 if player B wins, 0 if a draw
	 */
	public War(List<Integer> deck) {
		this.deck = new ArrayList<Integer>(deck);
		this.spoil = new ArrayList<Integer>();
		this.player1AHand = new ArrayList<Integer>();
		this.player2BHand = new ArrayList<Integer>();
		this.battles = 0;
	}

	public int run() {
		dealCards();
		topCards.add(3);
		while (battles < 1000) {
			if (player1AHand.size() == 0 && player2BHand.size() > 0)
				return -1;

			if (player1AHand.size() > 0 && player2BHand.size() == 0)
				return 1;

			if (player1AHand.size() == 0 && player2BHand.size() == 0)
				return 0;

			if (player1AHand.size() > 0 && player2BHand.size() > 0) {
				spoil.add(player1AHand.remove(0));
				spoil.add(player2BHand.remove(0));
			}
			if (spoil.size() > 0) {
				int result = battle(spoil.get(0), spoil.get(1));
				if (result == 5)
					return 0;

				if (result == 1) {
					player1AHand.addAll(spoil);
					spoil.clear();
				}
				if (result == -1) {
					player2BHand.addAll(spoil);
					spoil.clear();
				}
				if (result == 0) {
					int drawCheck = playDraw();
					if (drawCheck == -1)
						return -1;

					if (drawCheck == 1)
						return 1;

					if (drawCheck == 3)
						return 0;
				}
			}
		}
		return 0;
	}

	public int playDraw() {
		if (battles >= 1000) {
			return 3;
		}
		if (player1AHand.size() < 4 && player2BHand.size() >= 4) {
			return -1;
		}
		if (player2BHand.size() < 4 && player1AHand.size() >= 4) {
			return 1;
		} else if (player1AHand.size() >= 4 && player2BHand.size() >= 4) {
			for (int i = 0; i < 3; i++)
				spoil.add(player1AHand.remove(0));

			for (int i = 0; i < 3; i++)
				spoil.add(player2BHand.remove(0));

			spoil.add(player1AHand.remove(0));
			spoil.add(player2BHand.remove(0));
			int result = battle(spoil.get(spoil.size() - 2), spoil.get(spoil.size() - 1));
			if (result == 1) {
				player1AHand.addAll(spoil);
				spoil.clear();
			}
			if (result == -1) {
				player2BHand.addAll(spoil);
				spoil.clear();
			} else if (result == 0)
				playDraw();

		}
		return 0;
	}

	public void dealCards() {
		topCards = new ArrayList<Integer>(Arrays.asList(5, 5, 2, 4));
		for (int i = 0; i < deck.size(); i++) {
			if (i % 2 == 0) {
				player1AHand.add(deck.get(i));
			}
			if (i % 2 != 0) {
				player2BHand.add(deck.get(i));
			}
		}
	}

	public int battle(int a, int b) {
		if (deck.equals(topCards))
			return 5;

		battles++;
		if (a > b)
			return 1;

		if (b > a)
			return -1;

		return 0;
	}

	public static int findWinner(List<Integer> deck) {
		War w = new War(deck);
		return w.run();
	}

}
