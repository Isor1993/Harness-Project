/*****************************************************************************
* Project : LaneDefender
* File    : LaneDefender.cpp
* Date    : 09.09.2026
* Author  : Eric Rosenberg
*
* Description :
* Learning sandbox for the C++ course (L2): first console program, basic
* types and SAE naming practice. Becomes the game's entry point once
* milestone M1 starts.
*
* History :
* 09.09.2026 ER Created
* 11.09.2026 ER Added PrintMessage overloads and LoseLives, int32_t switch
* 12.09.2026 ER Added ReadValueInput with validated lives input (U4)
* 12.09.2026 ER Switched PrintMessage string params to const references (L3)
******************************************************************************/

#include <iostream>
#include <string>
#include <cstdint>
#include <limits>
#include <cstdlib>

/// <summary>
/// Prints a message followed by an integer value.
/// </summary>
/// <param name="a_sMessage">Text before the value.</param>
/// <param name="a_iPrintValue">Value printed after the text.</param>
/// <param name="a_bNextLine">True also ends the line.</param>
void PrintMessage(const std::string& a_sMessage, int32_t a_iPrintValue, bool a_bNextLine = true);

/// <summary>
/// Prints a message followed by a decimal value.
/// </summary>
/// <param name="a_sMessage">Text before the value.</param>
/// <param name="a_fPrintValue">Value printed after the text.</param>
/// <param name="a_bNextLine">True also ends the line.</param>
void PrintMessage(const std::string& a_sMessage, float a_fPrintValue, bool a_bNextLine = true);

/// <summary>
/// Prints an integer value on its own.
/// </summary>
/// <param name="a_iPrintValue">Value to print.</param>
/// <param name="a_bNextLine">True also ends the line.</param>
void PrintMessage(int32_t a_iPrintValue, bool a_bNextLine = true);

/// <summary>
/// Prints a decimal value on its own.
/// </summary>
/// <param name="a_fPrintValue">Value to print.</param>
/// <param name="a_bNextLine">True also ends the line.</param>
void PrintMessage(float a_fPrintValue, bool a_bNextLine = true);

/// <summary>
/// Prints a plain message.
/// </summary>
/// <param name="a_sMessage">Text to print.</param>
/// <param name="a_bNextLine">True also ends the line.</param>
void PrintMessage(const std::string& a_sMessage, bool a_bNextLine = true);

/// <summary>
/// Subtracts lost lives from the current lives.
/// </summary>
/// <param name="a_iCurrentLives">Lives before the hit.</param>
/// <param name="a_iLostLives">Lives taken by the hit.</param>
/// <returns>The remaining lives.</returns>
int32_t LoseLives(int32_t a_iCurrentLives, int32_t a_iLostLives);

/// <summary>
/// Asks for a number until the input is a valid amount of lives.
/// </summary>
/// <param name="a_iMinLives">Smallest accepted number of lives.</param>
/// <returns>The first valid number the player entered.</returns>
int32_t ReadValueInput(int32_t a_iMinLives);



int main()
{
	const int32_t I_LANE_MESSAGE_OFFSET = 1;
	const int32_t I_ZERO_LIVES = 0;
	const int32_t I_MAX_LANES = 3;
	const int32_t I_LIVES_LOST_PER_MONSTER = 1;
	const int32_t I_ADD_ROUND = 1;
	const int32_t I_MIN_LIVES = 1;

	int32_t iRounds = 1;
	
	

	PrintMessage("How many Lives the Player has?", true);

	int32_t iLives = ReadValueInput(I_MIN_LIVES);

	float fSpeed = 1.5f;

	bool bIsRoundRunning = true;
	std::string sPlayerName = "Isor";

	PrintMessage(sPlayerName, false);
	PrintMessage(" has ", iLives, false);
	PrintMessage(" lives and his speed is ", false);
	PrintMessage(fSpeed, true);

	PrintMessage("Round status: ", false);
	std::cout << std::boolalpha << bIsRoundRunning << std::endl;

	while (iLives > I_ZERO_LIVES)
	{
		for (int32_t i = 0;i < I_MAX_LANES;i++)
		{
			if (iLives <= I_ZERO_LIVES)
			{
				break;
			}
			PrintMessage(" Lane ", i + I_LANE_MESSAGE_OFFSET, true);

			iLives = LoseLives(iLives, I_LIVES_LOST_PER_MONSTER);

			PrintMessage("One monster went through. You lost ", I_LIVES_LOST_PER_MONSTER, false);
			PrintMessage(" Lives", true);

			PrintMessage(iLives, false);
			PrintMessage(" lives left.", true);
		}

		if (iLives > I_ZERO_LIVES)
		{
			PrintMessage(" Next Round is starting.", true);
		}
		else
		{
			PrintMessage(" Game Over in Round ", iRounds, true);

		}
		iRounds += I_ADD_ROUND;
	}
}

void PrintMessage(const std::string& a_sMessage, int32_t a_iPrintValue, bool a_bNextLine)
{
	if (a_bNextLine)
	{
		std::cout << a_sMessage << a_iPrintValue << std::endl;
		return;
	}
	std::cout << a_sMessage << a_iPrintValue;

}
void PrintMessage(const std::string& a_sMessage, float a_fPrintValue, bool a_bNextLine)
{
	if (a_bNextLine)
	{
		std::cout << a_sMessage << a_fPrintValue << std::endl;
		return;
	}
	std::cout << a_sMessage << a_fPrintValue;

}
void PrintMessage(int32_t a_iPrintValue, bool a_bNextLine)
{
	if (a_bNextLine)
	{
		std::cout << a_iPrintValue << std::endl;
		return;
	}
	std::cout << a_iPrintValue;

}
void PrintMessage(float a_fPrintValue, bool a_bNextLine)
{
	if (a_bNextLine)
	{
		std::cout << a_fPrintValue << std::endl;
		return;
	}
	std::cout << a_fPrintValue;

}
void PrintMessage(const std::string& a_sMessage, bool a_bNextLine)
{
	if (a_bNextLine)
	{
		std::cout << a_sMessage << std::endl;
		return;
	}
	std::cout << a_sMessage;
}

int32_t LoseLives(int32_t a_iCurrentLives, int32_t a_iLostLives)
{
	return a_iCurrentLives - a_iLostLives;
}

int32_t ReadValueInput(int32_t a_iMinLives)
{
	bool bValidInput = false;
	int32_t iInput = -1;

	while (true)
	{
		std::cin >> iInput;

		bValidInput = !std::cin.fail();

		if (!bValidInput)
		{
			std::cin.clear();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
			PrintMessage("Invalid Input!", true);
			continue;

		}
		if (iInput >= a_iMinLives)
		{
			std::system("cls");
			return iInput;
		}
		PrintMessage("Invalid Input!", true);
	}

}