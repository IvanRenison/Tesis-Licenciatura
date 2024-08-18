#### Monomios

Sea $X$ un alfabeto

Se define:

    $⟨X⟩ = X^*$

Se define el producto como la concatenación:

    $· : ⟨X⟩^2 → ⟨X⟩$

    $v · w = vw$

Y a $(⟨X⟩, ·)$ se lo llama monoide libre sobre $⟨X⟩$.

Sean $v, w ∈ ⟨X⟩$:

Se define:

    $v | w ⇔ ∃a , b ∈ ⟨X⟩ : w = avb$

#### Álgebra libre (asociativa):

Sean:

$R$ un anillo conmutativo

$X$ un alfabeto

Se define $R⟨X⟩$ la $R$-álgebra libre sobre $X$ como:

    $R⟨X⟩ = \{\sum_{i = 1}^n c_i w_i : c_1, …, c_n ∈ R, w_1, …, w_n ∈ ⟨X⟩\}$

La suma en $R⟨X⟩$ se define de la manera esperable.

El producto por escalares de define como:

    $c (\sum_{i = 1}^n c_i w_i) = (\sum_{i = 1}^n c c_i w_i)$

El producto entre elementos de $R⟨X⟩$ se define como:

    $(\sum_{i = 1}^n c_i w_i) · (\sum_{i = 1}^m c'_i w'_i) = \sum_{i = 1}^n \sum_{j = 1}^m c_i c'_j w_i w_j$

#### Cosas de los polinomios no conmutativos:

Sean:

$p ∈ R⟨X⟩$

$c_1, …, c_n ∈ R$

$w_1, …, w_n, w ∈ ⟨X⟩$

$f = \sum_{i = 1}^n c_i w_i$

Se define:

    $\text{coef}(f, w) = \left\{\begin{array}{ll} w = w_i → c_i \\ \text{si no} → 0  \end{array} \right. $ 

    $\text{sup}(f) = \{w_1, …, w_n\}$

#### Forman un anillo

$(R⟨X⟩, +, ·)$ es un anillo, por lo tanto aplican todas las definiciones de anillo
