up:
	docker-compose up $(s)

down:
	docker-compose down $(s)

run:
	docker-compose run $(s)

exec:
	docker-compose exec $(s)

update:
	docker-compose run --rm odoo odoo -u $(m) -d serviceminds --stop-after-init && docker-compose down

install:
	docker-compose run --rm odoo odoo -i $(m) -d serviceminds --stop-after-init && docker-compose down

psql:
	docker-compose exec db psql -U odoo serviceminds

shell:
	docker-compose exec odoo odoo shell -d serviceminds