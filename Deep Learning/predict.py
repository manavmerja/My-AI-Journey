{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "71738f49-c336-4956-9f97-4605fa761417",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Model loaded successfully!\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 159ms/step\n",
      "\n",
      "🤖 AI कहता है: यह नंबर 6 है!\n",
      "📄 असली जवाब: 6\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaEAAAGdCAYAAAC7EMwUAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAGb5JREFUeJzt3X9sVfX9x/HXFesF8fYuDbT3VkrTaJmLMBL53SE/jDTUrANhGUiylGUjOn5kpBq1Ywudf1BCIvGPTszMNx1ksrFliGQQsA7aslQECUTCDKuhrHXQNVR2bynQBvh8/yDceGktnMu9vHvb5yM5ib33vL0fzs54erj3HnzOOScAAAw8YL0AAMDQRYQAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAICZB60XcLsbN27o3LlzCgQC8vl81ssBAHjknFNnZ6dyc3P1wAP9X+sMuAidO3dOeXl51ssAANyj1tZWjRkzpt99BtwfxwUCAeslAACS4G5+P09ZhN5++20VFBRo+PDhmjRpkg4dOnRXc/wRHAAMDnfz+3lKIrRjxw6tXbtW69at0/Hjx/X000+rpKRELS0tqXg5AECa8qXiLtrTpk3TU089pS1btsQe+853vqOFCxeqqqqq39loNKpgMJjsJQEA7rNIJKLMzMx+90n6lVBPT4+OHTum4uLiuMeLi4vV2NjYa//u7m5Fo9G4DQAwNCQ9QhcuXND169eVk5MT93hOTo7a2tp67V9VVaVgMBjb+GQcAAwdKftgwu1vSDnn+nyTqqKiQpFIJLa1tramakkAgAEm6d8TGjVqlIYNG9brqqe9vb3X1ZEk+f1++f3+ZC8DAJAGkn4l9NBDD2nSpEmqra2Ne7y2tlZFRUXJfjkAQBpLyR0TysvL9eMf/1iTJ0/WjBkz9Lvf/U4tLS166aWXUvFyAIA0lZIILVmyRB0dHXrjjTd0/vx5jR8/Xnv37lV+fn4qXg4AkKZS8j2he8H3hABgcDD5nhAAAHeLCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzDxovQAAqfPYY48lNFdRUeF5ZtmyZZ5nnn32Wc8zjY2NnmcwcHElBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCY4QamQJoYM2aM55m9e/cm9FqPP/6455nr1697nrl27ZrnGQwuXAkBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGa4gSmQJn760596nknkRqSJqqmp8Txz5MiRFKwE6YQrIQCAGSIEADCT9AhVVlbK5/PFbaFQKNkvAwAYBFLyntCTTz6pjz76KPbzsGHDUvEyAIA0l5IIPfjgg1z9AADuKCXvCTU1NSk3N1cFBQVaunSpzpw58437dnd3KxqNxm0AgKEh6RGaNm2atm3bpv379+vdd99VW1ubioqK1NHR0ef+VVVVCgaDsS0vLy/ZSwIADFBJj1BJSYkWL16sCRMm6Nlnn9WePXskSVu3bu1z/4qKCkUikdjW2tqa7CUBAAaolH9ZdeTIkZowYYKampr6fN7v98vv96d6GQCAASjl3xPq7u7W559/rnA4nOqXAgCkmaRH6JVXXlF9fb2am5v1ySef6Ic//KGi0ajKysqS/VIAgDSX9D+O+/LLL/XCCy/owoULGj16tKZPn67Dhw8rPz8/2S8FAEhzPuecs17E10WjUQWDQetlACk1efJkzzMNDQ2eZxJ9v7WxsdHzTHFxseeZK1eueJ5B+ohEIsrMzOx3H+4dBwAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYSflfagegt8WLF3ueGT58uOeZI0eOeJ6RpAULFnie4WakSARXQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADDDXbSBe/Szn/3M88xrr73meaazs9PzzI9+9CPPM5L01VdfJTQHeMWVEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghhuYAl/j9/s9zyxevNjzjHPO88zrr7/ueaalpcXzDHA/cSUEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJjhBqbA18yfP9/zTHFxseeZjz76yPPMli1bPM8AAx1XQgAAM0QIAGDGc4QaGhpUWlqq3Nxc+Xw+7dq1K+5555wqKyuVm5urESNGaM6cOTp16lSy1gsAGEQ8R6irq0sTJ05UdXV1n89v2rRJmzdvVnV1tY4ePapQKKR58+aps7PznhcLABhcPH8woaSkRCUlJX0+55zTW2+9pXXr1mnRokWSpK1btyonJ0fbt2/Xiy++eG+rBQAMKkl9T6i5uVltbW1xnxby+/2aPXu2Ghsb+5zp7u5WNBqN2wAAQ0NSI9TW1iZJysnJiXs8Jycn9tztqqqqFAwGY1teXl4ylwQAGMBS8uk4n88X97Nzrtdjt1RUVCgSicS21tbWVCwJADAAJfXLqqFQSNLNK6JwOBx7vL29vdfV0S1+v19+vz+ZywAApImkXgkVFBQoFAqptrY29lhPT4/q6+tVVFSUzJcCAAwCnq+ELl26pC+++CL2c3Nzs06cOKGsrCyNHTtWa9eu1YYNG1RYWKjCwkJt2LBBDz/8sJYtW5bUhQMA0p/nCH366aeaO3du7Ofy8nJJUllZmX7/+9/r1Vdf1ZUrV7Ry5UpdvHhR06ZN04cffqhAIJC8VQMABgWfc85ZL+LrotGogsGg9TKQ5g4ePJjQ3Mcff+x55tZ34rx47rnnPM+cOXPG8wxgKRKJKDMzs999uHccAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzCT1b1YFUuG73/2u55nJkycn9FqzZs3yPJPIXbS5IzZwE1dCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZbmCKAe8vf/mL55mRI0cm9Fr79++/LzMD3RNPPOF5prOz0/PMf/7zH88zGFy4EgIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzHADUwx4hYWFnmeccwm91pYtWzzPXL161fPMt771Lc8zv/rVrzzPPPfcc55nJOnRRx/1PNPW1uZ55he/+IXnmX379nmewcDFlRAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYbmOK+mjlz5n15nZ6enoTmErkJZyJee+01zzOPPPKI55kTJ054npGkb3/7255nHn/8cc8zidwwtqCgwPMMBi6uhAAAZogQAMCM5wg1NDSotLRUubm58vl82rVrV9zzy5cvl8/ni9umT5+erPUCAAYRzxHq6urSxIkTVV1d/Y37zJ8/X+fPn49te/fuvadFAgAGJ88fTCgpKVFJSUm/+/j9foVCoYQXBQAYGlLynlBdXZ2ys7M1btw4rVixQu3t7d+4b3d3t6LRaNwGABgakh6hkpISvffeezpw4IDefPNNHT16VM8884y6u7v73L+qqkrBYDC25eXlJXtJAIABKunfE1qyZEnsn8ePH6/JkycrPz9fe/bs0aJFi3rtX1FRofLy8tjP0WiUEAHAEJHyL6uGw2Hl5+erqampz+f9fr/8fn+qlwEAGIBS/j2hjo4Otba2KhwOp/qlAABpxvOV0KVLl/TFF1/Efm5ubtaJEyeUlZWlrKwsVVZWavHixQqHwzp79qx++ctfatSoUXr++eeTunAAQPrzHKFPP/1Uc+fOjf186/2csrIybdmyRSdPntS2bdv0v//9T+FwWHPnztWOHTsUCASSt2oAwKDgc84560V8XTQaVTAYtF4GUuTQoUOeZ773ve95ntmzZ4/nGUkqLS1NaG6gSuSmp5J08uRJzzNjx45N6LW8WrBggeeZv/3tbylYCe4kEokoMzOz3324dxwAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMpPxvVgUs7Nq1y3oJA8Lw4cMTmrtfd8T+17/+5XmGO2IPLlwJAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmuIEpBjyfz+d5prCwMAUrGToSOeaJ2Llz5315HQxcXAkBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGa4gSkGPOec55mpU6cm9FpLly71PPPnP//Z88yNGzc8z2RkZHiemT59uucZKbFjfv36dc8zH3zwgecZDC5cCQEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZriBKe6rv//9755nxowZ43lm9uzZnmcSnfvBD37geWbHjh2eZ0pLSz3P/OQnP/E8k6h33nnH88yRI0dSsBKkE66EAABmiBAAwIynCFVVVWnKlCkKBALKzs7WwoULdfr06bh9nHOqrKxUbm6uRowYoTlz5ujUqVNJXTQAYHDwFKH6+nqtWrVKhw8fVm1tra5du6bi4mJ1dXXF9tm0aZM2b96s6upqHT16VKFQSPPmzVNnZ2fSFw8ASG+ePpiwb9++uJ9ramqUnZ2tY8eOadasWXLO6a233tK6deu0aNEiSdLWrVuVk5Oj7du368UXX0zeygEAae+e3hOKRCKSpKysLElSc3Oz2traVFxcHNvH7/dr9uzZamxs7PPf0d3drWg0GrcBAIaGhCPknFN5eblmzpyp8ePHS5La2tokSTk5OXH75uTkxJ67XVVVlYLBYGzLy8tLdEkAgDSTcIRWr16tzz77TH/84x97Pefz+eJ+ds71euyWiooKRSKR2Nba2prokgAAaSahL6uuWbNGu3fvVkNDQ9wXCUOhkKSbV0ThcDj2eHt7e6+ro1v8fr/8fn8iywAApDlPV0LOOa1evVo7d+7UgQMHVFBQEPd8QUGBQqGQamtrY4/19PSovr5eRUVFyVkxAGDQ8HQltGrVKm3fvl0ffPCBAoFA7H2eYDCoESNGyOfzae3atdqwYYMKCwtVWFioDRs26OGHH9ayZctS8gsAAKQvTxHasmWLJGnOnDlxj9fU1Gj58uWSpFdffVVXrlzRypUrdfHiRU2bNk0ffvihAoFAUhYMABg8fM45Z72Ir4tGowoGg9bLQIoMHz7c88zt/9FzN9544w3PM5I0adKkhObuh2/6cE9/Ev2/95dfful5ZurUqZ5n/vvf/3qeQfqIRCLKzMzsdx/uHQcAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAz3EUbg1JGRkZCc1OmTPE8s3nzZs8ziZzj7e3tnmc2btzoeUaSPvnkE88zX331VUKvhcGLu2gDAAY0IgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMNzAFAKQENzAFAAxoRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBlPEaqqqtKUKVMUCASUnZ2thQsX6vTp03H7LF++XD6fL26bPn16UhcNABgcPEWovr5eq1at0uHDh1VbW6tr166puLhYXV1dcfvNnz9f58+fj2179+5N6qIBAIPDg1523rdvX9zPNTU1ys7O1rFjxzRr1qzY436/X6FQKDkrBAAMWvf0nlAkEpEkZWVlxT1eV1en7OxsjRs3TitWrFB7e/s3/ju6u7sVjUbjNgDA0OBzzrlEBp1zWrBggS5evKhDhw7FHt+xY4ceeeQR5efnq7m5Wb/+9a917do1HTt2TH6/v9e/p7KyUr/5zW8S/xUAAAakSCSizMzM/ndyCVq5cqXLz893ra2t/e537tw5l5GR4f7617/2+fzVq1ddJBKJba2trU4SGxsbG1uab5FI5I4t8fSe0C1r1qzR7t271dDQoDFjxvS7bzgcVn5+vpqamvp83u/393mFBAAY/DxFyDmnNWvW6P3331ddXZ0KCgruONPR0aHW1laFw+GEFwkAGJw8fTBh1apV+sMf/qDt27crEAiora1NbW1tunLliiTp0qVLeuWVV/Txxx/r7NmzqqurU2lpqUaNGqXnn38+Jb8AAEAa8/I+kL7hz/1qamqcc85dvnzZFRcXu9GjR7uMjAw3duxYV1ZW5lpaWu76NSKRiPmfY7KxsbGx3ft2N+8JJfzpuFSJRqMKBoPWywAA3KO7+XQc944DAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwAwRAgCYIUIAADNECABghggBAMwQIQCAGSIEADBDhAAAZogQAMAMEQIAmCFCAAAzRAgAYIYIAQDMECEAgBkiBAAwQ4QAAGaIEADADBECAJgZcBFyzlkvAQCQBHfz+/mAi1BnZ6f1EgAASXA3v5/73AC79Lhx44bOnTunQCAgn88X91w0GlVeXp5aW1uVmZlptEJ7HIebOA43cRxu4jjcNBCOg3NOnZ2dys3N1QMP9H+t8+B9WtNde+CBBzRmzJh+98nMzBzSJ9ktHIebOA43cRxu4jjcZH0cgsHgXe034P44DgAwdBAhAICZtIqQ3+/X+vXr5ff7rZdiiuNwE8fhJo7DTRyHm9LtOAy4DyYAAIaOtLoSAgAMLkQIAGCGCAEAzBAhAICZtIrQ22+/rYKCAg0fPlyTJk3SoUOHrJd0X1VWVsrn88VtoVDIelkp19DQoNLSUuXm5srn82nXrl1xzzvnVFlZqdzcXI0YMUJz5szRqVOnbBabQnc6DsuXL+91fkyfPt1msSlSVVWlKVOmKBAIKDs7WwsXLtTp06fj9hkK58PdHId0OR/SJkI7duzQ2rVrtW7dOh0/flxPP/20SkpK1NLSYr20++rJJ5/U+fPnY9vJkyetl5RyXV1dmjhxoqqrq/t8ftOmTdq8ebOqq6t19OhRhUIhzZs3b9Ddh/BOx0GS5s+fH3d+7N279z6uMPXq6+u1atUqHT58WLW1tbp27ZqKi4vV1dUV22conA93cxykNDkfXJqYOnWqe+mll+Iee+KJJ9zrr79utKL7b/369W7ixInWyzAlyb3//vuxn2/cuOFCoZDbuHFj7LGrV6+6YDDo3nnnHYMV3h+3HwfnnCsrK3MLFiwwWY+V9vZ2J8nV19c754bu+XD7cXAufc6HtLgS6unp0bFjx1RcXBz3eHFxsRobG41WZaOpqUm5ubkqKCjQ0qVLdebMGeslmWpublZbW1vcueH3+zV79uwhd25IUl1dnbKzszVu3DitWLFC7e3t1ktKqUgkIknKysqSNHTPh9uPwy3pcD6kRYQuXLig69evKycnJ+7xnJwctbW1Ga3q/ps2bZq2bdum/fv3691331VbW5uKiorU0dFhvTQzt/73H+rnhiSVlJTovffe04EDB/Tmm2/q6NGjeuaZZ9Td3W29tJRwzqm8vFwzZ87U+PHjJQ3N86Gv4yClz/kw4O6i3Z/b/2oH51yvxwazkpKS2D9PmDBBM2bM0GOPPaatW7eqvLzccGX2hvq5IUlLliyJ/fP48eM1efJk5efna8+ePVq0aJHhylJj9erV+uyzz/SPf/yj13ND6Xz4puOQLudDWlwJjRo1SsOGDev1XzLt7e29/otnKBk5cqQmTJigpqYm66WYufXpQM6N3sLhsPLz8wfl+bFmzRrt3r1bBw8ejPurX4ba+fBNx6EvA/V8SIsIPfTQQ5o0aZJqa2vjHq+trVVRUZHRqux1d3fr888/Vzgctl6KmYKCAoVCobhzo6enR/X19UP63JCkjo4Otba2Dqrzwzmn1atXa+fOnTpw4IAKCgrinh8q58OdjkNfBuz5YPihCE/+9Kc/uYyMDPd///d/7p///Kdbu3atGzlypDt79qz10u6bl19+2dXV1bkzZ864w4cPu+9///suEAgM+mPQ2dnpjh8/7o4fP+4kuc2bN7vjx4+7f//738455zZu3OiCwaDbuXOnO3nypHvhhRdcOBx20WjUeOXJ1d9x6OzsdC+//LJrbGx0zc3N7uDBg27GjBnu0UcfHVTH4ec//7kLBoOurq7OnT9/PrZdvnw5ts9QOB/udBzS6XxImwg559xvf/tbl5+f7x566CH31FNPxX0ccShYsmSJC4fDLiMjw+Xm5rpFixa5U6dOWS8r5Q4ePOgk9drKysqcczc/lrt+/XoXCoWc3+93s2bNcidPnrRddAr0dxwuX77siouL3ejRo11GRoYbO3asKysrcy0tLdbLTqq+fv2SXE1NTWyfoXA+3Ok4pNP5wF/lAAAwkxbvCQEABiciBAAwQ4QAAGaIEADADBECAJghQgAAM0QIAGCGCAEAzBAhAIAZIgQAMEOEAABmiBAAwMz/A5dx0d1bb+WPAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# 1. मॉडल लोड करना (सीधा फाइल से)\n",
    "# हमें मॉडल का स्ट्रक्चर दोबारा बनाने की ज़रूरत नहीं है\n",
    "model = tf.keras.models.load_model('digit_recognizer.keras')\n",
    "\n",
    "print(\"✅ Model loaded successfully!\")\n",
    "\n",
    "# 2. टेस्ट के लिए कोई इमेज लेना\n",
    "# (अभी के लिए हम MNIST से ही एक इमेज ले लेते हैं चेक करने के लिए)\n",
    "mnist = tf.keras.datasets.mnist\n",
    "(_, _), (x_test, y_test) = mnist.load_data()\n",
    "x_test = x_test / 255.0\n",
    "\n",
    "# चलिए कोई एक रैंडम इमेज चुनते हैं (जैसे इमेज नंबर 50)\n",
    "image_index = 50\n",
    "test_image = x_test[image_index].reshape(1, 28, 28, 1) # Shape: (1, 28, 28, 1)\n",
    "\n",
    "# 3. भविष्यवाणी (Prediction) 🔮\n",
    "prediction = model.predict(test_image)\n",
    "predicted_digit = np.argmax(prediction)\n",
    "\n",
    "print(f\"\\n🤖 AI कहता है: यह नंबर {predicted_digit} है!\")\n",
    "print(f\"📄 असली जवाब: {y_test[image_index]}\")\n",
    "\n",
    "# 4. सबूत (Show Image)\n",
    "plt.imshow(x_test[image_index], cmap='gray')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff27a485-83ee-4388-8e24-c2ef40ae739b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
