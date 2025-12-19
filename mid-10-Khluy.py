{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPb4Cl82Sl/HR9+YJhLRUzc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KTeenLnwza007/10---Coding-68/blob/main/mid-10-Khluy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z0Q0t73ou_uF",
        "outputId": "126b6e7b-604c-4887-ac23-e0b403cba61d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ป้อนค่า ระยะทาง: 50\n",
            "ป้อนค่า เวลา: 12\n",
            "ขับรถเร็วเกินไป\n"
          ]
        }
      ],
      "source": [
        "#Input\n",
        "s = float(input(\"ป้อนค่า ระยะทาง: \"))\n",
        "t = float(input(\"ป้อนค่า เวลา: \"))\n",
        "\n",
        "# Process\n",
        "v = (s*t)\n",
        "\n",
        "#Output\n",
        "if v > 120:\n",
        "  print(\"ขับรถเร็วเกินไป\")\n",
        "else:\n",
        "  print(\"ไม่ขับรถเร็วอะดีแล้วนะคนดี\")"
      ]
    }
  ]
}