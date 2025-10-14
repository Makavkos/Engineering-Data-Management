# EDA датасета рецептур пива домашних пивоваров 
## Основная информация о датасете 
Датасет содержит информацию о стиях пива, приготовленного домашними пивоварам и основные характеристики получившегося продукта.

- **Количество записей**: 73861
- **Количество признаков**: 23
  
Пояснение к столбцам:

`BeerID` - идентификатор рецепта

`Name` - название пива

`Style` - стиль пива

`Size(L)` - объем партии 

`OG` - начальная экстрактивность сусла 

`FG` - конечная экстрактивность сусла 

`ABV` - крепость 

`IBU` - единицы горечи

`Color` - цветность

`BrewMethod` - метод варки

`SugarScale` - содержание сахаров в пиве

`Efficiency` - эффективность затирания 

`MashThickness` - велечина пеннной шапки

`BrewMethod` - Метот варки пива 

`PitchRate` - Количество внесенных дрожжей 

`PrimaryTemp` - температура брожения 

`PrimingMethod` - Метод карбонизации 

`PrimingAmount` - Количество карбонизирующего агента

## Оценка структуры
Датасет выгружался из хранилища Google disk


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BeerID</th>
      <th>Name</th>
      <th>URL</th>
      <th>Style</th>
      <th>StyleID</th>
      <th>Size(L)</th>
      <th>OG</th>
      <th>FG</th>
      <th>ABV</th>
      <th>IBU</th>
      <th>...</th>
      <th>BoilGravity</th>
      <th>Efficiency</th>
      <th>MashThickness</th>
      <th>SugarScale</th>
      <th>BrewMethod</th>
      <th>PitchRate</th>
      <th>PrimaryTemp</th>
      <th>PrimingMethod</th>
      <th>PrimingAmount</th>
      <th>UserId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Vanilla Cream Ale</td>
      <td>/homebrew/recipe/view/1633/vanilla-cream-ale</td>
      <td>Cream Ale</td>
      <td>45</td>
      <td>21.77</td>
      <td>1.055</td>
      <td>1.013</td>
      <td>5.48</td>
      <td>17.65</td>
      <td>...</td>
      <td>1.038</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>NaN</td>
      <td>17.78</td>
      <td>corn sugar</td>
      <td>4.5 oz</td>
      <td>116.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Southern Tier Pumking clone</td>
      <td>/homebrew/recipe/view/16367/southern-tier-pumk...</td>
      <td>Holiday/Winter Special Spiced Beer</td>
      <td>85</td>
      <td>20.82</td>
      <td>1.083</td>
      <td>1.021</td>
      <td>8.16</td>
      <td>60.65</td>
      <td>...</td>
      <td>1.070</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>955.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Zombie Dust Clone - EXTRACT</td>
      <td>/homebrew/recipe/view/5920/zombie-dust-clone-e...</td>
      <td>American IPA</td>
      <td>7</td>
      <td>18.93</td>
      <td>1.063</td>
      <td>1.018</td>
      <td>5.91</td>
      <td>59.25</td>
      <td>...</td>
      <td>NaN</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>Specific Gravity</td>
      <td>extract</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Zombie Dust Clone - ALL GRAIN</td>
      <td>/homebrew/recipe/view/5916/zombie-dust-clone-a...</td>
      <td>American IPA</td>
      <td>7</td>
      <td>22.71</td>
      <td>1.061</td>
      <td>1.017</td>
      <td>5.80</td>
      <td>54.48</td>
      <td>...</td>
      <td>NaN</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Bakke Brygg Belgisk Blonde 50 l</td>
      <td>/homebrew/recipe/view/89534/bakke-brygg-belgis...</td>
      <td>Belgian Blond Ale</td>
      <td>20</td>
      <td>50.00</td>
      <td>1.060</td>
      <td>1.010</td>
      <td>6.48</td>
      <td>17.84</td>
      <td>...</td>
      <td>1.050</td>
      <td>72.0</td>
      <td>NaN</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>NaN</td>
      <td>19.00</td>
      <td>Sukkerlake</td>
      <td>6-7 g sukker/l</td>
      <td>18325.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>

### Приведение типов данных 
Проверял тип данных и сохранял в новые типы столбцы, для которых это было нужно 

Изначальные типы данных:

<img width="360" height="699" alt="image" src="https://github.com/user-attachments/assets/4830f928-c68a-4c14-8953-5a5567f89ee1" />

Конечный результат:

<img width="401" height="718" alt="image" src="https://github.com/user-attachments/assets/757d7191-19ca-4a3f-839c-1fd096a2bd01" />

Name, URL, PrimingAmount не изменял, так как значения в них слишком хаотичные, включающие буквы и цифры, так что ни под Категории, ни под что-то еще они не подходят.

## Работа с пропусками и повторами 
### Работа с пропусками 
Вывел информацию по пропускам в каждом из столбцов:

<img width="319" height="664" alt="image" src="https://github.com/user-attachments/assets/61c1ea32-d292-4aea-bd58-26dae5896c56" />

Обратил внимание, что в столбцах MashThickness, PitchRate, PrimaryTemp, PrimingMethod, PrimingAmount очень большое количество пропусков. Решил посмотреть какое процентное соотношение эти пропуски имеют в сравнении с общим количеством записей:

<img width="621" height="164" alt="image" src="https://github.com/user-attachments/assets/bec5ff17-a26b-48fc-b1a6-88bf638d6c5c" />

Из-за большого количества пропусков решил удалить столбцы: MashThickness, PrimingMethod, PrimingAmount, PitchRate

Так как колонки URL, BeerID, UserId не несут полезной информации и в некоторых из них также много пропусков, их тоже удаляем

Вид датасета после удаления колонок:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Style</th>
      <th>StyleID</th>
      <th>Size(L)</th>
      <th>OG</th>
      <th>FG</th>
      <th>ABV</th>
      <th>IBU</th>
      <th>Color</th>
      <th>BoilSize</th>
      <th>BoilTime</th>
      <th>BoilGravity</th>
      <th>Efficiency</th>
      <th>SugarScale</th>
      <th>BrewMethod</th>
      <th>PrimaryTemp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Vanilla Cream Ale</td>
      <td>Cream Ale</td>
      <td>45</td>
      <td>21.77</td>
      <td>1.055</td>
      <td>1.013</td>
      <td>5.48</td>
      <td>17.65</td>
      <td>4.83</td>
      <td>28.39</td>
      <td>75</td>
      <td>1.038</td>
      <td>70.0</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>17.78</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Southern Tier Pumking clone</td>
      <td>Holiday/Winter Special Spiced Beer</td>
      <td>85</td>
      <td>20.82</td>
      <td>1.083</td>
      <td>1.021</td>
      <td>8.16</td>
      <td>60.65</td>
      <td>15.64</td>
      <td>24.61</td>
      <td>60</td>
      <td>1.070</td>
      <td>70.0</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Zombie Dust Clone - EXTRACT</td>
      <td>American IPA</td>
      <td>7</td>
      <td>18.93</td>
      <td>1.063</td>
      <td>1.018</td>
      <td>5.91</td>
      <td>59.25</td>
      <td>8.98</td>
      <td>22.71</td>
      <td>60</td>
      <td>NaN</td>
      <td>70.0</td>
      <td>Specific Gravity</td>
      <td>extract</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Zombie Dust Clone - ALL GRAIN</td>
      <td>American IPA</td>
      <td>7</td>
      <td>22.71</td>
      <td>1.061</td>
      <td>1.017</td>
      <td>5.80</td>
      <td>54.48</td>
      <td>8.50</td>
      <td>26.50</td>
      <td>60</td>
      <td>NaN</td>
      <td>70.0</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bakke Brygg Belgisk Blonde 50 l</td>
      <td>Belgian Blond Ale</td>
      <td>20</td>
      <td>50.00</td>
      <td>1.060</td>
      <td>1.010</td>
      <td>6.48</td>
      <td>17.84</td>
      <td>4.57</td>
      <td>60.00</td>
      <td>90</td>
      <td>1.050</td>
      <td>72.0</td>
      <td>Specific Gravity</td>
      <td>All Grain</td>
      <td>19.00</td>
    </tr>
  </tbody>
</table>
</div>

### Работа с дубликатами 
<img width="383" height="43" alt="image" src="https://github.com/user-attachments/assets/015bdd47-ded6-485b-a347-58d40717af22" />

Считаю, что эти повторы не влияют на датасет, так как многие характеристики могут иметь схожие значения или повторяться. к тому же 117 повторов на более 70 000 записей - мало, с моей точки зрения. Оставляю без внимания.

## Работа с выбросами 
Найдем выбросы по IQR. Анализируем колонки IBU, ABV, OG, FG, Color

<Figure size 1500x1000 with 4 Axes><img width="1489" height="989" alt="image" src="https://github.com/user-attachments/assets/cf456093-3a51-4da2-a3cf-4dbbe020020a" />

<Figure size 640x480 with 1 Axes><img width="552" height="413" alt="image" src="https://github.com/user-attachments/assets/f5b276b2-8c8b-4e7c-bf7f-22f0275cdd9c" />

Из визуального осмотра делаю вывод, что выбросов много, однако в случае с колонками начальной и конечной экстрактивности (OG, FG соответсвенно), цветностью Color они не критичны, так как эти показатели могут принимать достаточно большие значения. В случае с Крепостью (ABV) и горечью IBU нужно принять меры. Пиво крепостью более 15 градусов - маловероятно. Гочерь более 100 единиц не воспринимается рецепторами. В связи с этим принимаю решение удалить часть значений. Также теперь датасет сохранен как clean_data.

Удаление значений ABV более 20 %:

<img width="308" height="258" alt="image" src="https://github.com/user-attachments/assets/0eaa07f7-8661-448f-9178-80daa2674435" />

Удаление значений IBU более 150: 

<img width="295" height="255" alt="image" src="https://github.com/user-attachments/assets/d767a2e1-6b8a-411f-a14e-9e309a83261d" />

## Корреляции
Для проверки взаимосвязи характеристик построим матрицу корреляций:
<Figure size 1200x1000 with 2 Axes><img width="1104" height="1003" alt="image" src="https://github.com/user-attachments/assets/29343718-c3ab-4b87-8fb9-a42255c7dd92" />

Данные имеют очень слабую взаимосвязь. Исключения - Удельный вес сусла (BoilGravity) и экстрактивность сусла, а также объем варки и конечный объем продукта. 
