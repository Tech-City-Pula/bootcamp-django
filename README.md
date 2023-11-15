## U terminalu prvo napravis svoj direktorij

```bash
mkdir django_aplikacija
```

## Koristeci i dalje terminal odes u taj direktorij

```bash
cd django_aplikacija
```

## Napravis virtualni environment koristeci `venv` komandu


```bash
python3 -m venv django-env
```

## Aktiviras virtualni environment

windows

```cmd
django-env\Scripts\activate
```

mac/linux
```bash
source django-env/bin/activate
```


## Instaliras `django`

```bash
python3 -m pip install django
```

## Koristeci `django-admin` generiras svoj projekt

```bash
django-admin startproject moj_projekt
```

## Koristeci i dalje terminal odes u svoj projekt

```bash
cd moj_projekt
```

## Za pokretanje servera koristis `manage.py` program dajuci mu komandu `runserver`

```bash
# unutar `moj_projekt` foldera
python3 manage.py runserver
```

## Za dodavanje nove aplikacije unutar projekta koristis `manage.py` program dajuci mu komandu `startapp` i ime aplikacije


```bash
# unutar `moj_projekt` foldera
python3 manage.py startapp moja_aplikacija
```