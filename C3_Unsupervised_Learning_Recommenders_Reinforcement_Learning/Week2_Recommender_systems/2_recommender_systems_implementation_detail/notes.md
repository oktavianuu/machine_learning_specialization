# Recommender System Implementation Detail

## Mean Normalization
| Movie | Alice | Bob | Carol | Dave | Eve |
|-------|-------|-----|-------|------|-----|
| Love at last | 5 | 5 | 0 | 0 | ? |
| Romance forever | 5 | ? | ? | 0 | ? |
| Cute puppies of love | ? | 4 | 0 | ? | ? |
| Nonstop car chases| 0 | 0 | 5 | 4 | ? |
| Swords vs. Karate | 0 | 0 | 5 | ? | ? |

Without mean normalization, new user will always have zero. Normalization helps predicting the movie rating by new users. Then how to do the mean normalization? Here is how:
1. We took all the rating values there and put them into two dimensional matrix as follow:
$$
\begin{bmatrix}
5&5&0&0&? \\
5&?&?&0&? \\
?&0&4&?&? \\
0&0&5&4&? \\
0&0&5&0&?
\end{bmatrix}
$$
2. Then we compute the average of each movie:
movie 1: `[5 5 0 0 ?]`, there are two `5s` and two `0s`. Therefore the `total = 10` with `n = 4`. Then `10/4 = 2.5`. Then we do all the same thing to other movie which resulting the following vector:

$$
\mu = \begin{bmatrix}
2.5 \\
2.5 \\
2 \\
2.25 \\
1.25
\end{bmatrix}
$$

3. Then we substract the mean from every rating as follow:

$$
\begin{bmatrix}
5&5&0&0&? \\
5&?&?&0&? \\
?&0&4&?&? \\
0&0&5&4&? \\
0&0&5&0&?
\end{bmatrix}
- 
\begin{bmatrix}
2.5 \\
2.5 \\
2 \\
2.25 \\
1.25
\end{bmatrix}
=
\begin{bmatrix}
2.5&2.5&-2.5&-25&? \\
2.5&?&?&-2.5&? \\
?&2&-2&?&? \\
-2.25&-2.25&2.75&1.75&? \\
-1.25&-1.25&3.75&-1.25&?
\end{bmatrix}
$$

4. Using the new calculated value, we can learn $w_j, v_j$ and $x_i$.

5. Then we can predict:
For user `j`, on movie `i` predict:
$w^{(j)}$ . $x^{(i)}$ + $b^{(j)}$ + $\mu_i$

From this, the new user, `user 5` will be calculated as follow:

$$
w^{(5)} = \begin{bmatrix}
0 \\
0
\end{bmatrix}
, 
b^{(5)} = [0]
$$
then
$w^{(5)}$ . $x^{(1)}$ + $b^{(5)}$ + $\mu_1$ = 2.5 
**IMPORTANT: NOT YET FINISHED**

## Tensorflow Implementation of Collaborative Filtering



## Finding Related Items



