# fake-ap

Sahte erişim noktaları yapmaya yarayan bir araçtır.

## Gereksinimler

ssh-brute aşağıdaki kütüphaneleri kullanır.

* Colorama
* Faker
* Scapy

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/fake-ap.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -i        | Interface. Kullanılacak ağ arayüzünü belirtmek için kullanılır. |
```bash
sage: fake-ap.py [-h] [-i I]

options:
  -h, --help  show this help message and exit
  -i Interface
```

## Örnekler

```python
python3 fake-ap.py -i wlan0mon
```
