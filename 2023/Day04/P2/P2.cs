using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace P2
{
	static class Counter
	{
		public static int value;
	}

	class Program
	{
		static void Main()
		{
			string inputFile = "input.txt";
			List<string> lines = File.ReadAllLines(inputFile).ToList();

			List<Card> cards = new List<Card>();
			Dictionary<int, int> cardDict = new Dictionary<int, int>();

			Counter.value = 1;

			foreach(string line in lines)
			{
				string[] card_parts = line.Split(':');
				string[] parts = card_parts[1].Split('|');
				string[] winningNumbers = parts[0].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(num => num.Trim()).ToArray();;
				string[] myNumbers = parts[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(num => num.Trim()).ToArray();

				Card  card = new Card(winningNumbers, myNumbers);
				cards.Add(card);
				cardDict.Add(card.Number, 1);
			}

			int totCards = cards.Count();
			Console.WriteLine($"totCards = {totCards}");
			int res = 0;

			foreach(Card card in cards)
			{
				Console.WriteLine($"Card {card.Number} : totWinner = {card.TotPoint} and nbOfTime = {cardDict[card.Number]}");
				for (int i = card.Number + 1; i <= card.Number + card.TotPoint && i <= totCards; i++)
				{
					cardDict[i] = cardDict[i] + cardDict[card.Number];
					//Console.WriteLine($"i = {i}");
				}
				res += cardDict[card.Number];
			}
			Console.WriteLine($"TOTAL : {res}");
		}
	}

	class Card
	{
		// Class members
		public int Number { get; private set; }
		public string[] WinNumbers { get; private set; }
		public string[] MyNumbers { get; private set; }
		public int TotPoint { get; private set; }

		// Class constructor
		public Card(string[] winningNumbers, string[] myNumbers)
		{
			this.WinNumbers = winningNumbers;
			this.MyNumbers = myNumbers;

			/*
			   Console.WriteLine($"WinNumbers :");
			   foreach(string nb in this.WinNumbers)
			   Console.WriteLine($"nb = {nb}");
			   Console.WriteLine($"MyNumbers :");
			   foreach(string nb in this.MyNumbers)
			   Console.WriteLine($"nb = {nb}");
			   */
			this.TotPoint = 0;
			this.TotPoint = this.CalculatePoints();
			this.Number = Counter.value++;
		}

		// Class function members
		private int CalculatePoints()
		{
			foreach(string number in this.MyNumbers)
			{
				//Console.WriteLine($"My number : {number}");
				if (this.WinNumbers.Contains(number))
				{
						this.TotPoint++;
				}
			}
			return this.TotPoint;
		}
	}
}
