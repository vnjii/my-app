SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM film
	JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM category
	JOIN film_category ON category.category_id = film_category.category_id
	JOIN film ON film_category.film_id = film.film_id
WHERE film.rental_rate = 2.99
	AND category.name = 'Drama';

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM actor
	JOIN film_actor ON actor.actor_id = film_actor.actor_id
	JOIN film ON film_actor.film_id = film.film_id
	JOIN film_category ON film.film_id = film_category.film_id
	JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = 'Sandra'
	AND actor.last_name = 'Kilmer'
	AND category.name = 'Action';
