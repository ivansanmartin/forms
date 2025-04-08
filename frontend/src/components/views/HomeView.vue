<template>
	<Header></Header>
	<div class="d-flex flex-column justify-content-evenly h-100">
		<div class="hero-section text-center">
			<div class="container">
				<h1 class="display-4 fw-bold">
					Create Forms Without Registration
				</h1>
				<p class="lead text-muted">
					Generate and manage forms easily with a unique URL.
				</p>
				<a href="/create-form" class="btn btn-primary btn-lg mt-3">
					<i class="fas fa-plus-circle me-2"></i> Create Form
				</a>
			</div>
		</div>
		<div class="features-section text-center py-5">
			<div class="container">
				<div class="row">
					<div class="col-md-4">
						<i class="fas fa-plus-circle feature-icon"></i>
						<h3 class="mt-3">Easy to Use</h3>
						<p>Create a form in seconds and share it with a URL.</p>
					</div>
					<div class="col-md-4">
						<i class="fas fa-edit feature-icon"></i>
						<h3 class="mt-3">Simple Management</h3>
						<p>Edit and manage responses effortlessly.</p>
					</div>
					<div class="col-md-4">
						<i class="fas fa-chart-bar feature-icon"></i>
						<h3 class="mt-3">Real-Time Metrics</h3>
						<p>View response statistics in real-time.</p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<Footer></Footer>
</template>

<script setup>
import Header from '@/components/layout/Header.vue';
import Footer from '@/components/layout/Footer.vue';
</script>

<style scoped></style>
